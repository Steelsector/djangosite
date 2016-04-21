/**
 * Created by steel on 2016. 04. 08..
 */
//alert('asdsa');
$(document).ready(function () {

    var circlesCreated = false;

    function onScroll() {
        if (!circlesCreated && $('#skills').visible()) {
            circlesCreated = true;
            createCircles();
        }
    }

    function createCircles() {
        $('.precent').each(function (i, obj) {

            var child = this.id;
            percentage = this.getAttribute('value') / 100;
            $("#" + child).circleProgress({
                value: percentage,
                size: 80,
                fill: {
                    gradient: ["navy", "turquoise"]
                }
            }).on('circle-animation-progress', function (event, progress) {
                $(this).find('strong').html(parseInt(this.getAttribute('value') * progress) + '<i>%</i>'
                )
                ;
            });
        });
    }

    if ($('#skills').visible() != true) {
        window.onscroll = onScroll;
    } else {
        createCircles();
    }

});