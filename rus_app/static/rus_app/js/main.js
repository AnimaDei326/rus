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
        //return false;
    });

    $('.responsive .main-menu a').click(function () {
        $('.responsive .main-menu').hide();

    });

    // $('.main-menu').singlePageNav();


    $(document).ready(function test() {
        $('#form-contact').submit(function () { // catch the form's submit event
            $.ajax({ // create an AJAX call...
                data: $(this).serialize(), // get the form data
                type: $(this).attr('method'), // GET or POST
                url: $(this).attr('action'), // the file to call
                success: function (response) { // on success..
                    $('.contact-form').html(response);
                    test();
                }
            });
            return false;
        });
    });

    function add_more() {
        // нижняя граница документа
        let windowRelativeBottom = document.documentElement.getBoundingClientRect().bottom;

        let last_card = $('.card-detail').last();

        let offset = last_card.offset();
        let bottom = $(window).height() - last_card.height();
        bottom = bottom - offset.top
        let add = 800;

        if (windowRelativeBottom < bottom + add) {
            // добавим больше данных

            let offset_id = last_card.attr('id');
            $.ajax({ // create an AJAX call...
                data: $(this).serialize(), // get the form data#}
                type: 'GET', // GET or POST
                url: '/blogs_/?offset=' + offset_id, // the file to call
                success: function (response) { // on success..

                        response['blogs'].forEach((item) => {
                            let html = '<div class="card card-detail" id="' + item.id + '">' +
                                '<a href="/blog/{{ item.code }}/">' +
                                '<img class="card-img card-img-detail za" src="' + item.picture +'" alt="' + item.title +'">';
                                if (item.title)
                                    html += '<h5 class="card-title-detail">' + item.title + '</h5>';
                                if (item.preview_text)
                                    html += '<p class="card-text-detail">' + item.preview_text + '</p>';
                                html += '</a></div>';

                            $('.card-columns').append(html);
                        })
                    }
            });
            window.removeEventListener('scroll', add_more);
            window.setTimeout(function () {
                window.addEventListener('scroll', add_more);
            }, 2000)
        }
    }

    window.addEventListener('scroll', add_more);
    // TODO vem если только на странице блога

})(window, jQuery);
