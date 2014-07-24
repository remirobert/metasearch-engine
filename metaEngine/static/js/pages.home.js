$(document).ready(function() {

    $('#home-select').click(function() {
        $('#home-platforms').slideToggle({duration:'fast'});
        $('#logo-box').slideToggle({duration:'fast'});
    });

    $('#home-platforms ul li a').click(function(e) {
        e.preventDefault();

	//var type = platform.val("toto");
        $('#home-select span').text($(this).attr("data-platform-name"));
        $('#home-search input[name="platform"]').attr("value", $(this).attr("data-platform"));

        $('#home-platforms').slideToggle({duration:'fast'});
        $('#logo-box').slideToggle({duration:'fast'});
    });

    $('#search-buttons button.go').mouseup(function(e) {
        e.preventDefault();
        $('#home-search form').submit();
    });

    $('#search-buttons button.random').mouseup(function(e) {
        e.preventDefault();
        $('#home-search form').attr('action', $('#home-search form').attr('action')+'/random')
        $('#home-search form').submit();
    });

    $('a.btn-navbar').click(function() {
        $('.nav').slideToggle({duration:'fast'});
    });

    // Home resize.
    home_position();

    $(window).resize(function() {
        home_position();
    });

    // Set focus
    $('#home-input').focus();
    
});

function home_position() {

    // Manage height of the page to center the content.
    var window_h = $(window).height();
    var topbar_h = $('.navbar').height();
    var botbar_h = $('#bottom').height();
    var global_h = $('#homepage #global').height();
    var search_h = $('#home-logo').height() + $('#home-search').height()+ $('.search-nb').height() + 100;

    var content_h = window_h-(topbar_h+botbar_h);
    var margin_top = ((content_h-search_h)/2)+(topbar_h-botbar_h)-46;


    if(margin_top > 10) {
        $('#home-logo').css('margin-top', margin_top);
    }

    console.log("Window height: "+window_h);
    console.log("Topbar height: "+topbar_h);
    console.log("Bottombar height: "+botbar_h);
    console.log("Global height: "+global_h);
    console.log("Search height: "+search_h);
    console.log("Content height: "+content_h);
    console.log("Margin top: "+margin_top);
    console.log("Search nb: "+$('.search-nb').height());

}
