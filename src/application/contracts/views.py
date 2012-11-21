"""
This module contains the views used by the contracts package
"""
from flask import render_template, flash, url_for, redirect, request, jsonify

from application import app

import models, forms

from application.accounts.accounts import require_roles, find_users
from application.accounts.models import UserRoleModel, RoleModel

from flaskext.flask_login import login_required, current_user

import urllib

import datetime as dt

@app.route('/contracts/list')
@app.route('/contracts')
@login_required
def contracts_list_contracts():
    """
    Lists all of the available contracts
    and provides links to their summary pages
    """

    can_edit = None
    query = UserRoleModel.all()
    query.filter('user =', current_user.key())

    uroles = query.fetch(query.count())
    for urole in uroles:
        if urole.role.name == 'webmaster':
            can_edit = True
            break
        

    query = models.ContractModel.all()
    
    contracts = query.fetch(query.count())

    for contract in contracts:
        contract.url_name = urllib.quote_plus(contract.name)
    
    return render_template('contracts/list.html',
                           can_edit=can_edit,
                           contracts=contracts)

@app.route('/contracts/<contract_name>')
@login_required
def contracts_show_contract(contract_name):
    """
    Shows a summary of the contract requirements.
    If the user has not signed a contract it also
    displays a signup button
    """

    can_edit = None
    query = UserRoleModel.all()
    query.filter('user =', current_user.key())

    uroles = query.fetch(query.count())
    for urole in uroles:
        if urole.role.name == 'webmaster':
            can_edit = True
            break

    query = models.SignedContractModel.all()
    query.filter('user =', current_user.key())

    can_sign = None
    if query.count() == 0:
        can_sign = True
            
    query = models.ContractModel.all()
    query.filter('name =', urllib.unquote_plus(contract_name))

    try:
        contract = query.fetch(1)[0]
    except IndexError:
        return render_template('404.html'), 404

    contract.url_name = contract_name
        
    query = models.TimeReqModel.all()
    query.filter('contract_ =', contract.key())

    time_reqs = query.fetch(query.count())

    for time_req in time_reqs:
        time_req.str_time = str(time_req.time)
        time_req.str_date = str(time_req.dueDate)
        time_req.url_name = urllib.quote_plus(time_req.name)

    query = models.DuesReqModel.all()
    query.filter('contract_ =', contract.key())

    dues_reqs = query.fetch(query.count())

    for dues_req in dues_reqs:
        dues_req.str_date = str(dues_req.dueDate)
        dues_req.url_name = urllib.quote_plus(dues_req.name)

    return render_template('contracts/show.html',
                           can_edit=can_edit,
                           can_sign=can_sign,
                           contract=contract,
                           time_reqs=time_reqs,
                           dues_reqs=dues_reqs)

@app.route('/contracts/progress')
@login_required
def contracts_progress():
    """
    Shows the contract progress for the current user
    """

    query = models.SignedContractModel.all()
    query.filter('user =', current_user.key())

    try:
        signed_contract = query.fetch(1)[0]
    except IndexError:
        flash('You have not yet signed a contract', 'error')
        return redirect(url_for('contracts_list'))

    query = models.TimeReqProgressModel.all()
    query.filter('user =', current_user.key())

    time_req_progresses = query.fetch(query.count())
    for time_req_progress in time_req_progresses:
        time_req_progress.str_prog_time = str(time_req_progress.time)
        time_req_progress.str_req_time = str(time_req_progress.req.time)
        time_req_progress.str_due_date = str(time_req_progress.req.dueDate)
        time_req_progress.str_time_left = str(time_req_progress.req.dueDate - dt.date.today())
        time_req_progress.complete = (time_req_progress.req.time <= time_req_progress.time)
        
    query = models.DuesReqProgressModel.all()
    query.filter('user =', current_user.key())

    dues_req_progresses = query.fetch(query.count())
    for dues_req_progress in dues_req_progresses:
        dues_req_progress.str_due_date = str(dues_req_progress.req.dueDate)
        dues_req_progress.str_time_left = str(dues_req_progress.req.dueDate - dt.date.today())
        dues_req_progress.complete = (dues_req_progress.req.amount <= dues_req_progress.amount)
    
    return render_template('contracts/progress.html',
                           user=current_user,
                           contract=signed_contract.contract_,
                           time_req_progs=time_req_progresses,
                           dues_req_progs=dues_req_progresses)
                           

@app.route('/contracts/<contract_name>/sign')
@login_required
def contracts_sign(contract_name):
    """
    Allows a user that has not already signed a contract
    to sign a contract
    """

    query = models.SignedContractModel.all()
    query.filter('user =', current_user.key())


    if query.count() != 0:
        flash('You cannot sign more than one contract', 'error')
        return redirect(url_for('contracts_list'))

    query = models.ContractModel.all()
    query.filter('name =', urllib.unquote_plus(contract_name))

    try:
        contract = query.fetch(1)[0]
    except:
        return render_template('404.html'), 404

    signed = models.SignedContractModel(user=current_user.key(),
                                        contract_ = contract.key())

    signed.put()

    # create the empty progress models for each requirement on this contract
    query = models.TimeReqModel.all()
    query.filter('contract_ =', contract)

    time_reqs = query.fetch(query.count())
    for time_req in time_reqs:
        time_req_prog = models.TimeReqProgressModel(user=current_user.key(),
                                                    req=time_req)
        time_req_prog.put()

    query = models.DuesReqModel.all()
    query.filter('contract_ =', contract)
        
    dues_reqs = query.fetch(query.count())
    for dues_req in dues_reqs:
        dues_req_prog = models.DuesReqProgressModel(user=current_user.key(),
                                                    req=dues_req)
        dues_req_prog.put()

    flash('You have successfully signed a contract', 'success')
    return redirect(url_for('contracts_progress'))

@app.route('/contracts/create', methods=['GET','POST'])
@require_roles(names=['webmaster'])
def contracts_create_contract():
    """
    Creates a new contract
    """

    new_contract_form = forms.ContractForm()
    if request.method == 'POST' and new_contract_form.validate():
        contract = models.ContractModel(name=new_contract_form.name.data,
                                        desc=new_contract_form.desc.data)
        contract.put()

        name = urllib.quote_plus(contract.name)
        
        return redirect(url_for('contracts_show_contract',
                                contract_name=name))
    else:
        return render_template('contracts/create.html',
                               form=new_contract_form)

@app.route('/contracts/<contract_name>/create/<url_type>', methods=['GET', 'POST'])
@require_roles(names=['webmaster'])
def contracts_create_req(contract_name, url_type):
    """
    Creates a new time requirement
    """

    query = models.ContractModel.all()
    query.filter('name =', urllib.unquote_plus(contract_name))

    try:
        contract = query.fetch(1)[0]
    except IndexError:
        return render_template('404.html'), 404

    contract.url_name = contract_name

    if url_type == "time-req":
        type = "Time"
        form = forms.TimeReqForm()
        if request.method == 'POST' and form.validate():
            new_req = models.TimeReqModel(contract_=contract,
                                          dueDate=form.due_date.data,
                                          name=form.name.data,
                                          time=dt.time(form.hours.data))
            new_req.put()

            # create progress models for the new requirement
            for signed in contract.signedcontractmodel_set:
                new_req_prog = models.TimeReqProgressModel(user=signed.user.key(),
                                                           req=new_req.key())
                new_req_prog.put()
            
            return redirect(url_for('contracts_show_contract',
                                    contract_name=contract_name))
        else:
            return render_template('contracts/create_req.html',
                                   contract=contract,
                                   time=True,
                                   type=type,
                                   url_type=url_type,
                                   form=form)
    elif url_type == "dues-req":
        type = "Dues"
        form = forms.DuesReqForm()
        if request.method == 'POST' and form.validate():
            new_req = models.DuesReqModel(contract_=contract,
                                          dueDate=form.due_date.data,
                                          name=form.name.data,
                                          amount=form.amount.data)
            new_req.put()

            # create progress models for the new requirement
            for signed in contract.signedcontractmodel_set:
                new_req_prog = models.DuesReqProgressModel(user=signed.user.key(),
                                                           req=new_req.key())
                new_req_prog.put()
            
            return redirect(url_for('contracts_show_contract',
                                    contract_name=contract_name))                            
        else:
            return render_template('contracts/create_req.html',
                                   contract=contract,
                                   type=type,
                                   url_type=url_type,
                                   form=form)            
    else:
        return render_template('404.html'), 404

@app.route('/contracts/<contract_name>/<req_name>/delete/<url_type>', methods=['GET'])
@require_roles(names=['webmaster'])
def contracts_delete_req(contract_name, req_name, url_type):
    """
    Deletes the specified requirement
    """

    query = models.ContractModel.all()
    query.filter('name =', urllib.unquote_plus(contract_name))
    try:
        contract = query.fetch(1)[0]
    except IndexError:
        return render_template('404.html'), 404

    if url_type == 'time-req':
        query = models.TimeReqModel.all()
        query.filter('contract_ =', contract.key())
        query.filter('name =', urllib.unquote_plus(req_name))

        try:
            req = query.fetch(1)[0]
        except IndexError:
            return render_template('404.html'), 404

        for req_prog in req.timereqprogressmodel_set:
            req_prog.delete()

        req.delete()
    elif url_type == 'dues-req':
        query = models.DuesReqModel.all()
        query.filter('contract_ =', contract.key())
        query.filter('name =', urllib.unquote_plus(req_name))

        try:
            req = query.fetch(1)[0]
        except IndexError:
            return render_template('404.html'), 404

        for req_prog in req.duesreqprogressmodel_set:
            req_prog.delete()

        req.delete()
    else:
        return render_template('404.html'), 404

    return redirect(url_for('contracts_show_contract',
                            contract_name=contract_name))


@app.route('/contracts/<contract_name>/delete')
@require_roles(names=['webmaster'])
def contracts_delete_contract(contract_name):
    """
    Allows an administrator to delete a contract
    and all of its requirements
    """
    
    query = models.ContractModel.all()
    query.filter('name =', urllib.unquote_plus(contract_name))
    try:
        contract = query.fetch(1)[0]
    except IndexError:
        return render_template('404.html'), 404

    for req in contract.reqmodel_set:
        if isinstance(req, models.TimeReqModel):
            for req_prog in req.timereqprogressmodel_set:
                req_prog.delete()
        elif isinstance(req, models.DuesReqModel):
            for req_prog in req.duesreqprogressmodel_set:
                req_prog.delete()
        req.delete()

    for signed_contract in contract.signedcontractmodel_set:
        signed_contract.delete()

    contract.delete()

    return redirect(url_for('contracts_list_contracts'))

@app.route('/contracts/delete/signed')
def contracts_delete_signed():
    """
    Remove me in the final version
    """
    query = models.SignedContractModel.all()
    signed = query.fetch(query.count())
    for sign in signed:
        for req_prog in sign.user.reqprogressmodel_set:
            req_prog.delete()
        sign.delete()

    return redirect(url_for('contracts_list_contracts'))