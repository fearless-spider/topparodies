var o = {
    init: function(){
        this.diagram();
    },
    random: function(l, u){
        return Math.floor((Math.random()*(u-l+1))+l);
    },
    diagram: function(){
        var W = $(window).width()/1170;
        if (W >= 1) {
            W = 1;
        }
        var r = new Raphael('diagram', 320*W, 320*W),
            rad = 65*W;

        r.circle(150*W, 150*W, 75*W).attr({ stroke: 'none', fill: '#193340' });

        var title = r.text(150*W, 150*W, 'Najedź na\nkolory').attr({
            font: '18px Arial',
            fill: '#fff'
        }).toFront();

        r.customAttributes.arc = function(value, color, rad){
            var v = 3.6*value,
                alpha = v == 360 ? 359.99 : v,
                random = o.random(91, 240),
                a = (random-alpha) * Math.PI/180,
                b = random * Math.PI/180,
                sx = 150*W + rad * Math.cos(b),
                sy = 150*W - rad * Math.sin(b),
                x = 150*W + rad * Math.cos(a),
                y = 150*W - rad * Math.sin(a),
                path = [['M', sx, sy], ['A', rad, rad, 0, +(alpha > 180), 1, x, y]];
            return { path: path, stroke: color }
        }

        $('.get').find('.arc').each(function(i){
            var t = $(this),
                color = t.find('.color').val(),
                value = t.find('.percent').val(),
                text = t.find('.text').text();

            rad += 24*W;
            var z = r.path().attr({ arc: [value, color, rad], 'stroke-width': 20*W });

            z.mouseover(function(){
                this.animate({ 'stroke-width': 50*W, opacity: .75 }, 1000, 'elastic');
                if(Raphael.type != 'VML') //solves IE problem
                    this.toFront();
                title.animate({ opacity: 0 }, 500, '>', function(){
                    this.attr({ text: text + '\nstron/wejście' }).animate({ opacity: 1 }, 500, '<');
                });
            }).mouseout(function(){
                    this.animate({ 'stroke-width': 20*W, opacity: 1 }, 1000, 'elastic');
                });
        });
    }
};
$(function(){ o.init(); });
/* BACK TO TOP
 ================================================== */

$(document).ready(function() {

    // Some options for customization
    var leftgap = 0;		/* gap on the left */
    var rightgap = 224;		/* gap on the right */
    var defaultgap = 400;	/* the intro gap */
    var caption = true;		/* toggle caption */
    var reveal = 0.5;		/* define 0 - 1 far does it goes to reveal the second caption */

    // find each of the .beforeafter
    $('.beforeafter').each(function () {

        // set current selected item to variable
        var i = $(this);
        // get the source of the first image and second image using eq(index)
        var img_mask = i.children('img:eq(0)').attr('src');
        var img_bg = i.children('img:eq(1)').attr('src');

        // get the caption for the first image as default caption
        var img_cap_one = i.children('img:eq(0)').attr('alt');
        var W = $(window).width()/1170,
            H = $(window).height()/1170;
        // get the dimension of the first image, assuming second image has the same dimension
        var width = i.children('img:eq(1)').width();
        var height = 600;//i.children('img:eq(0)').height();
        var width2 = i.children('img:eq(0)').width();
        var height2 = 337;//i.children('img:eq(0)').height();
        if (W < 1.0) {
            width = i.children('img:eq(1)').width()*W;
            height = 600*W;//i.children('img:eq(0)').height();
            width2 = i.children('img:eq(0)').width()*W;
            height2 = 337*W;
            $('.beforeafter').width(width).height(height);
            defaultgap = defaultgap * W;
            rightgap = rightgap * W;
        } else {
            W = 1;
        }
        // hide the images, not removing it because we will need it later
        i.find('img').css('visibility','hidden');

        // set some css attribute to current item
        i.css({'overflow': 'hidden', 'position': 'relative'});

        // append additional html element
        i.append('<div class="ba-mask"><button id="slider" class="btn socle"></button></div>');
        i.append('<div class="ba-bg"></div>');
        i.append('<div class="ba-caption badge">' + img_cap_one + '</div>');

        // set the dimension of appended html element
        i.children('.ba-mask').width(width2);
        i.children('.ba-mask').height(height2);
        i.children('.ba-bg').width(width);
        i.children('.ba-bg').height(height);
        i.children('.ba-mask').css('left',113*W+'px').css('top',56*W+'px').css('right',114*W+'px');
        i.children('.ba-caption').css('bottom',80*W + 'px');
        i.children('.ba-mask').children('#slider').height(30*W).width(30*W).css('right',-10*W+'px');
        // set the images as background for ba-mask and ba-bg
        i.children('.ba-mask').css('backgroundImage','url(' + img_mask + ')');
        i.children('.ba-bg').css('backgroundImage','url(' + img_bg + ')');

        // animate to reveal the background image
        i.children('.ba-mask').animate({'width':width - defaultgap}, 1000);

        // if caption is true, then display it, otherwise, hide it
        if (caption) i.children('.caption').show();
        else i.children('.ba-caption').hide();

    }).mousemove(function (e) {

            // set current selected item to variable
            var i = $(this);
            var slider = $('#slider');
            slider.css('margin-top','0px').css('margin-bottom','0px');

            // get the position of the image
            pos_img = i.offset()['left'];

            // get the position of the mouse pointer
            pos_mouse = e.pageX;

            // calculate the difference between the image and cursor
            // the difference will the width of the mask image
            new_width = pos_mouse - pos_img;
            img_width = i.width();
            var W = $(window).width()/1170;
            if (W >= 1) {
                W = 1;
            }
            if (e.pageY-i.offset()['top'] <= 337*W) {
                slider.css('top', e.pageY-i.offset()['top']-15*W + 'px');
            }
            // get the captions for first and second images
            img_cap_one = i.children('img:eq(0)').attr('alt');
            img_cap_two = i.children('img:eq(1)').attr('alt');

            /*
             // for debugging purposes
             $('#debug').html("X Axis : " + e.pageX + " | Y Axis " + e.pageY);
             $('#debug2').html(i.position()['left']);
             $('#debug3').html(new_width);
             */

            // make sure it reveal the image and left some gaps on left and right
            // it depends on the value of leftgap and rightgap
            if (new_width > leftgap && new_width < (img_width - rightgap)) {
                i.children('.ba-mask').width(new_width);
            }

            // toggle between captions.
            // it uses the reveal variable to calculate
            // eg, display caption two once the image is 50% (0.5) revealed.
            if (new_width < (img_width * reveal)) {
                i.children('.ba-caption').html(img_cap_two);
            } else {
                i.children('.ba-caption').html(img_cap_one);
            }

        }).bind('touchmove',function(e){
            e.preventDefault();
            // set current selected item to variable
            var touch = e.originalEvent.touches[0] || e.originalEvent.changedTouches[0];

            var i = $(this);
            var slider = $('#slider');
            slider.css('margin-top','0px').css('margin-bottom','0px');

            // get the position of the image
            pos_img = i.offset()['left'];

            // get the position of the mouse pointer
            pos_mouse = touch.pageX;

            // calculate the difference between the image and cursor
            // the difference will the width of the mask image
            new_width = pos_mouse - pos_img;
            img_width = i.width();
            var W = $(window).width()/1170;
            if (W >= 1) {
                W = 1;
            }
            if (touch.pageY-i.offset()['top'] <= 337*W) {
                slider.css('top', touch.pageY-i.offset()['top']-15*W + 'px');
            }
            // get the captions for first and second images
            img_cap_one = i.children('img:eq(0)').attr('alt');
            img_cap_two = i.children('img:eq(1)').attr('alt');

            /*
             // for debugging purposes
             $('#debug').html("X Axis : " + e.pageX + " | Y Axis " + e.pageY);
             $('#debug2').html(i.position()['left']);
             $('#debug3').html(new_width);
             */

            // make sure it reveal the image and left some gaps on left and right
            // it depends on the value of leftgap and rightgap
            if (new_width > leftgap && new_width < (img_width - rightgap)) {
                i.children('.ba-mask').width(new_width);
            }

            // toggle between captions.
            // it uses the reveal variable to calculate
            // eg, display caption two once the image is 50% (0.5) revealed.
            if (new_width < (img_width * reveal)) {
                i.children('.ba-caption').html(img_cap_two);
            } else {
                i.children('.ba-caption').html(img_cap_one);
            }
        });
});