$(document).ready(function() {
    // console.log("worked")
   
    
    // $('.carousel').carousel({
    //     interval: 3000
    //   })
    // alert("iii")

    $(".click_me").on('click', function(){
        window.location = "contact_us#post";    
   });






    $("window").scroll(function() {
        alert("yesss boiiiu")
        console.log("yes")
        // $(".navbar-collapse").toggleClass("show");
        // $(".navbar-toggler").toggleClass("collapsed");

    });

    $(".clr").mouseenter(function() {
        
        // alert("start")
        $(".nav-container").toggleClass("grad");
        $(".nav-container").toggleClass("clicked");

    });

    $(".clr").mouseleave(function() {
        $(".nav-container").toggleClass("clicked");
        $(".nav-container").toggleClass("grad");
        
    });

//     $(".post-link").on('click', function(){
//         window.location = "/ind_posts/{{ post.id }}";    
//    });


});

// console.log("new")
// function resize() {
//     if ($(window).width() < 1200) {
//      console.log("yeah boi")
//      $('#chill').addClass('col-5');
//     }
//     else {$('#chill').removeClass('col-5');}
// }

// $(document).ready( function() {
//     $(window).resize(resize);
//     resize();
// });


$(document).click(function() {
    // alert('clicked outside');
    
    if ($(".navbar-collapse").hasClass("show")) {
        // alert("has show ")
        $(".navbar-collapse").toggleClass("show");
    }
});


// $(document).click(function() {
//     alert('clicked outside');

// });

// $(".navbar-collapse").click(function(event) {
//     $(".navbar-collapse").toggleClass("show");
//     $(".navbar-toggler").toggleClass("collapsed");
//     // alert('clicked inside');
//     event.stopPropagation();
// });

// $(document).click(function(event) { 
//     $target = $(event.target);
//     if(!$target.closest('#navbar-collapse').length && 
//     $('#navbar-collapse').is(":visible")) {
//       $('#navbar-collapse').hide();
//     }        
// });
// $(document).click(function(event) { 
//     $target = $(event.target);
//     if(!$target.closest('#navbar-toggler').length && 
//     $('#navbar-toggler').is(":visible")) {
//       $('#navbar-toggler').hide();
//     }        
// });

// document.getElementById("navbar").onmouseover = function () { mouseOver() };
// document.getElementById("navbar").onmouseout = function () { mouseOut() };

// function mouseOver() {
//     document.getElementById("navbar").setAttribute("style", "background-color: rgba(0, 0, 0, 0.47)");

// }

// function mouseOut() {
//     document.getElementById("navbar").setAttribute("style", "background-color: rgba(193, 66, 66, 0)");
// }