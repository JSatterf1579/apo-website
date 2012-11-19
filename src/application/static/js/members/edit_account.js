$(document).ready(function() {
    window.pendingRequests = 0;
    window.requestErrors = false;

    $('.save-button').click(function() {
	$('form').each(function() {
	    window.pendingRequests++;
	    window.requestErrors = false;
	    $('.formval-error').remove()
	    $.post(this.action, $(this).serialize(),
		   processData);
	});
    });
});

function processData(data)
{
    window.pendingRequests--; // decrement the request counter
    if(window.pendingRequests <= 0) // if this is the last request
    {
	if(!window.requestErrors) // if there were no errors display success message
	{
	    var lastAlert = $('.alert:last');
	    var newAlert = $('<div></div>', {'class': 'alert alert-success'});
	    newAlert.append('<i class="icon-ok-sign"></i>&nbsp;');
	    newAlert.append('<a class="close" data-dismiss="alert">x</a>');
	    newAlert.append('Successfully saved');

	    if(lastAlert.length <= 0)
	    {
		$('#maincontent').prepend(newAlert);
	    }
	    else
	    {
		lastAlert.after(newAlert);
	    }
	}
	else // if there were errors display error message
	{
	    var lastAlert = $('.alert:last');
	    var newAlert = $('<div></div>', {'class': 'alert alert-error'});
	    newAlert.append('<i class="icon-exclamation-sign"></i>&nbsp;');
	    newAlert.append('<a class="close" data-dismiss="alert">x</a>');
	    newAlert.append('Error saving data see below');

	    if(lastAlert.length <= 0)
	    {
		$('#maincontent').prepend(newAlert);
	    }
	    else
	    {
		lastAlert.after(newAlert);
	    }
	}
    }
    else // more requests to process
    {
	if(data.result != 'success') // an error has occurred
	{
	    window.requestErrors = true;
	

	    var form = $('#'+data.name);
	    for(var key in data.errors)
	    {
		if (data.errors.hasOwnProperty(key))
		{
		    var dd = $('#'+key, form).parent();
		    if( $('.formval-error', dd).length <= 0)
		    {
			dd.append('<ul class="formval-error"></ul>');
		    }
		    $('.formval-error', dd).append('<li>' + data.errors[key] + '</li>');
		}
	    }
	}
    }
}

