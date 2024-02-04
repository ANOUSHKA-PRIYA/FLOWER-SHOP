jQuery(document).ready(function($) {
    $('.hero').slick({
        dots: false,
        infinite: true,
        speed: 500,
        fade: !0,
        cssEase: 'linear',
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 8000,
        draggable: true,
        arrows: true,
        prevArrow: '<div class="arrow-left"><span class="slick-mark slick-prev"></span></div>',
        nextArrow: '<div class="arrow-right"><span class="slick-mark slick-next"></span></div>',
        responsive: [{
            breakpoint: 1200,
            settings: {
                arrows: false,
                dots: true,
            }
        }, {
            breakpoint: 1024,
            settings: {
                infinite: true,
                arrows: false,
                dots: true,
            }
        }, {
            breakpoint: 768,
            settings: {
                arrows: false,
                dots: true,
            }
        }, {
            breakpoint: 600,
            settings: {
                arrows: false,
                dots: true,
            }
        }, {
            breakpoint: 480,
            settings: {
                arrows: false,
                dots: true,
            }
        }]
    });
});

jQuery(document).ready(function() {
    $('.feature__slider--box').slick({
        infinite: true,
        speed: 500,
        slidesToShow: 4,
        slidesToScroll: 1,
        draggable: true,
        arrows: false,
        swipeToSlide: true,
        responsive: [{
            breakpoint: 992,
            settings: {
                slidesToShow: 3,
            }
        }, {
            breakpoint: 768,
            settings: {
                slidesToShow: 2,
            }
        }, {
            breakpoint: 576,
            settings: {
                slidesToShow: 2,
            }
        }, {
            breakpoint: 320,
            settings: {
                slidesToShow: 1,
            }
        }]
    });

    $('.feature__nav--prev').click(function() {
        $('.feature__slider--box').slick('slickPrev');
    });

    $('.feature__nav--next').click(function() {
        $('.feature__slider--box').slick('slickNext');
    });

    $('.new__slider--box').slick({
        infinite: true,
        speed: 500,
        slidesToShow: 4,
        slidesToScroll: 1,
        draggable: true,
        arrows: false,
        swipeToSlide: true,
        responsive: [{
            breakpoint: 992,
            settings: {
                slidesToShow: 3,
            }
        }, {
            breakpoint: 768,
            settings: {
                slidesToShow: 2,
            }
        }, {
            breakpoint: 576,
            settings: {
                slidesToShow: 2,
            }
        }, {
            breakpoint: 320,
            settings: {
                slidesToShow: 1,
            }
        }]
    });

    $('.new__nav--prev').click(function() {
        $('.new__slider--box').slick('slickPrev');
    });

    $('.new__nav--next').click(function() {
        $('.new__slider--box').slick('slickNext');
    });
});

jQuery(document).ready(function() {
    $('.section__quote--box').slick({
        dots: true,
        infinite: true,
        speed: 500,
        slidesToShow: 1,
        slidesToScroll: 1,
        draggable: true,
        arrows: false,
        swipeToSlide: true,
    });
});