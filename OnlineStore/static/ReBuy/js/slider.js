// Product slider

var productSlideIndex = 1;
showProductSlides(productSlideIndex);

function plusProductSlides(n) {
    showProductSlides(productSlideIndex += n);
}


function showProductSlides(n) {
    var i;
    var productSlides = document.getElementsByClassName('product_slide');

    if (n > productSlides.length) {
        productSlideIndex = 1;
    }
    if (n < 1) {
        productSlideIndex = productSlides.length;
    }
    for (i = 0; i < productSlides.length; i++){
        productSlides[i].style.display = "none";
    }
    productSlides[productSlideIndex - 1].style.display = "block";
}

