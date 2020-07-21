$(document).ready(function () {
    $(window).scroll(function () {
        if($(this).scrollTop() > 20){
            alert("hi")
        $('#topBtn').fadeIn();
    }else{
        $('#topBtn').fadeOut();
    }

    });
    $('#topBtn').click(function () {
        $('html, body').animate({scrollTop:0},800);


    });
});