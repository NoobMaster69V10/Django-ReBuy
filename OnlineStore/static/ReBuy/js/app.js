
// Main Slider
var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
    showSlides(slideIndex += n);
}


function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName('main_slide');

    if (n > slides.length) {
        slideIndex = 1;
    }
    if (n < 1) {
        slideIndex = slides.length;
    }
    for (i = 0; i < slides.length; i++){
        slides[i].style.display = "none";
    }
    slides[slideIndex - 1].style.display = "block";
}



// Main second slider

var dailySlide = document.getElementById('dailySlide');
var dailyInner = document.getElementById('dailyInner');
var offset = 0;

function dailyNext(){
    if ( offset < 2400 ){
        offset += 1200;
        dailyInner.scrollLeft = offset;
    }
    else if(offset >= 2400){
        offset = 0;
        dailyInner.scrollLeft = offset;
    }
}
function dailyPrev(){
    if ( offset <= 0 ){
        offset = 2400;
        dailyInner.scrollLeft = offset; 
    }
    else if(offset > 0){
        offset -= 1200;
        dailyInner.scrollLeft = offset;
    }
}
