setTimeout(function(){
    $("p.container2").slideUp();
    $("p.container2").slideDown();
    
},2000);

setTimeout(function(){
    $("img.p-img").slideUp();
    $("img.p-img").slideDown();
    $("h4.text-animation").animate({
        opacity : 1
    });
},2000);

// setTimeout(function () {
//     $("p.container2").slideUp();
// }, 2000);
// setTimeout(function () {
//     $("p.container2").slideDown();
// }, 2000);
// clearTimeout("p.container2");
// $("p.container2").animation({
//     color : "red"
// }, 5000);
// $('selector expression').animate({ stylePropertyName : 'value'},
//                                 duration,
//                                 easing, 
//                                 callback);