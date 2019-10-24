function phoneMask() { 
    var num = $(this).val().replace(/\D/g,''); 
    $(this).val(num.substring(0,1) + '(' + num.substring(1,2) + ')' + " " + num.substring(2,6) + '-' + num.substring(6,12)); 
}
$('[type="tel"]').keyup(phoneMask);