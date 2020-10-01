$("p").hide();


$(document).ready(function(){
    $("#login").click(function(){
        if($('#inputUsername').val()=='admin' && $('#inputPassword').val()=='password'){
            location.replace("/admin")
        }else{
            $("p").show();
        }
    });
  });