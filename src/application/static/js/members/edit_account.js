$(document).ready(function() {
    $('.save-button').click(function() {
	$('form').each(function() {
	    $('.formval-error').remove()
	    $.post(this.action, $(this).serialize(),
		   processData);
	});
    });
});

function processData(data)
{
    if(data.result != 'success')
    {
	console.log(data.errors);
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

