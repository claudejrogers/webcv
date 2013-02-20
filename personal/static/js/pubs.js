$('.li-expand').addClass('li-expand-off');

$('.li-expand').click(function() {
    if ($(this).hasClass('li-expand-off')) {
        $(this).removeClass('li-expand-off');
        $(this).addClass('li-expand-on');
    } else {
        $(this).removeClass('li-expand-on');
        $(this).addClass('li-expand-off');
    }
});
