$('#login').submit(function(e){
    var valid= true,
    errorMessage= "";

    if($('#username').val() == ''){
        errorMessage = "* Please Enter Correct Username \n";
        $('.userid').text(errorMessage).show();
        valid= false;
    }
    else{
        $('.userid').text(errorMessage).hide();
        valid= true;
    }

    if($('#password').val() == ''){
        errorMessage = "* Incorrect Password \n";
        $('.pwd').text(errorMessage).show();
        valid= false;
    }
    else{
        $('.pwd').text(errorMessage).hide();
        valid= true;
    }

    return valid;
});