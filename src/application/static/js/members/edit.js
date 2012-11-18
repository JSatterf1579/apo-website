$(document).ready(function(){
    $('#email-addbutton').click(function() {
	addForm('#emails');
    });
    
    $('#address-addbutton').click(function() {
	addForm('#addresses');
    });
    
    $('#phone-addbutton').click(function() {
	addForm('#phones');
    });
});

function addForm(selector){
    // clone the form list

    var lastnode = $(selector+' dl:last').clone(true);

    var inputs = $('input', lastnode);

    for(var i=0; i < inputs.length; i++)
    {
	inputs[i].setAttribute("id", plusone(inputs[i].getAttribute("id")));
	inputs[i].setAttribute("name", plusone(inputs[i].getAttribute("name")));
	if(fieldName(inputs[i].getAttribute("id")) != 'csrf_token')
	{
	    inputs[i].setAttribute("value", "");
	}
    }
    
    var id = inputs[0].getAttribute("id");

    var minusbutton = '<button type="button" class="removeForm" onClick="removeForm($(this));">Delete</button>';

    $(selector+' div').append(lastnode);
    
    console.log($(selector+' div dl .removeForm').length);
    if($(selector+' div dl .removeForm').length == 0)
    {
	$(selector+' div dl:last').append(minusbutton);
    }
    
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

function fieldName(name){
    return new RegExp("(\\w+)-(\\d+)-(\\w+)", "gi").exec(name)[3];
}

function removeForm(obj){
    obj.parent().remove();
}