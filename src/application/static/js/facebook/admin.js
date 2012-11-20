$(document).ready(function() {
    $('input:checkbox').change(
	function(){
	    $('form').each(function() {
		$.post(this.action, $(this).serialize(),
		       processData);
	    });
	});
});

function processData(data)
{
    if(data.result != 'success') // an error has occurred
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
