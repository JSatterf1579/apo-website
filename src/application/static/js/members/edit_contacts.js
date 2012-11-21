$(document).ready(function(){
    $('#email-addbutton').click(function() {
	addForm('emails');
    });
    
    $('#address-addbutton').click(function() {
	addForm('addresses');
    });
    
    $('#phone-addbutton').click(function() {
	addForm('phones');
    });


});


function addForm(selector){
    // clone the form list
    var nodes = $('#'+selector+' dl:first');
    if(nodes.length == 1 && nodes.parent()[0].getAttribute('id') == selector)
    {
	var lastnode = $('#'+selector+' dl:last');
	var clonednode = lastnode.clone(true);
	lastnode.parent().remove();
    }
    else
    {
	var clonednode = $('#'+selector+' dl:last').clone(true);
	$('.hideForm', clonednode).remove();
	
	if($('.removeForm', clonednode).length == 0)
	{
	    clonednode.append('<button type="button" class="removeForm" onClick="removeForm($(this));">Delete</button>');
	}
    }

    $('#'+selector+' div').append(clonednode);

    renumber(clonednode.parent());
    
}

function plusone(str){
    return str.replace(
	new RegExp("-(\\d+)-", "gi"),
	function($0, $1){
	    var i = parseInt($1) + 1;
	    return "-" + i + "-";
	}
    );
}

function setIdNum(str, i){
    return str.replace(
	new RegExp("-(\\d+)-", "gi"),
	function($0, $1){
	    return "-" + i + "-";
	}
    );
}

function fieldName(name){
    return new RegExp("(\\w+)-(\\d+)-(\\w+)", "gi").exec(name)[3];
}

function removeForm(obj){
    // redo the numbering
    var div = obj.parent().parent();
    obj.parent().remove();
    renumber(div);
}

function hideForm(obj){
    var div = obj.parent().parent();
    var id = obj.parent().parent().parent().attr('id');
    $('#hiddenForms').append('<div id="' + id +'"></div>');
    $('#hiddenForms #'+id).append(obj.parent());
    renumber(div);
    
}

function renumber(obj){
    // redo the numbering of all of the children of the obj passed in
    var children = obj.children();
    for( var i=0; i<children.length; i++)
    {
	var inputs = $('input', children[i]);
	for(var j=0; j < inputs.length; j++)
	{
	    inputs[j].setAttribute("id", setIdNum(inputs[j].getAttribute("id"), i));
	    inputs[j].setAttribute("name", setIdNum(inputs[j].getAttribute("name"), i));
	}
    }
}