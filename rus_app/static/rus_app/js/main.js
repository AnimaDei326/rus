(function (window, $) {
    'use strict';

    // Cache document for fast access.
    var document = window.document;


    function mainSlider() {
        $('.bxslider').bxSlider({
            pagerCustom: '#bx-pager',
            mode: 'fade',
            nextText: '',
            prevText: '',
            autoStart: true,
            auto: true,
        });
    }

    mainSlider();


    var $links = $(".bx-wrapper .bx-controls-direction a, #bx-pager a");
    $links.click(function () {
        $(".slider-caption").removeClass('animated fadeInLeft');
        $(".slider-caption").addClass('animated fadeInLeft');
    });

    $(".bx-controls").addClass('container');
    $(".bx-next").addClass('fa fa-angle-right');
    $(".bx-prev").addClass('fa fa-angle-left');


    $('a.toggle-menu').click(function () {
        $('.responsive .main-menu').toggle();
        return false;
    });

    $('.responsive .main-menu a').click(function () {
        $('.responsive .main-menu').hide();

    });

    $('.main-menu').singlePageNav();

    // $(document).ready(function test() {
    //     $('#form-contact').submit(function () { // catch the form's submit event
    //         $.ajax({ // create an AJAX call...
    //             data: $(this).serialize(), // get the form data
    //             type: $(this).attr('method'), // GET or POST
    //             url: $(this).attr('action'), // the file to call
    //             success: function (response) { // on success..
    //                 $('.contact-form').html(response);
    //                 test();
    //
    //             }
    //         });
    //         return false;
    //     });
    //     $('#id_anti_email').type = 'email';
    // });

})(window, jQuery);
