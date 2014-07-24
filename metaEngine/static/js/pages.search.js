$(document).ready(function() {

    $('#search-select').click(function() {
        $('#search-platforms').slideToggle({duration:'fast'});
    });

    $('#search-platforms ul li a').click(function(e) {
        e.preventDefault();

        $('#search-select span').text($(this).attr("data-platform-name"));
        $('#top-search input[name="platform"]').attr("value", $(this).attr("data-platform"));

        $('#search-platforms').slideToggle({duration:'fast'});
    });


    // Fixes the button bug.
    $('#top-search button').mouseup(function(e) {
        e.preventDefault();
        $('#top-search form').submit();
    });

    $('button:submit.my-btn').mouseup(function(e) {
        e.preventDefault();
        $(this).parents('form:first').submit();
    });
    /*
    $('a.my-btn').mouseup(function(e) {
        e.preventDefault();
        
        if($(this).attr('target') == '_blank') {
            window.open($(this).attr("href"));
        } else {
            $(location).attr('href',$(this).attr("href"));
        }
        
    });
    */
    $('a.my-btn').mouseup(function(e) {
        e.preventDefault();
        
        if($(this).attr('target') == '_blank') {
            window.open($(this).attr("href"));
        } else {
            $(location).attr('href',$(this).attr("href"));
        }
        
    });

    // Required by Firefox to not open 2 windows onclick.
    $('a.my-btn span').mouseup(function(e) {
        e.preventDefault();
        
        $(this).parent().click(function(e) {
            e.preventDefault();
        });
    });

    // Set focus
    $('#top-search form input').focus();
    
    /**
     * Ajouter aux favoris
     * 
     * @param {type} event
     * @returns {undefined}
     */
    function addToFavorites(event) {
        
        // Stop l'évènement
        event.preventDefault();
        
        $(event.target).addClass('active');
        
        // Requête AJAX
        $.ajax({
            url: sub_url_base + 'ajax-request/users/addToFavorites',
            data: {url: $(event.target).attr('name').substring(13)},
            type: 'post'
         }).done(function(res) {
            res = jQuery.parseJSON(res);

            if (res.result == true) {
                $(event.target).unbind('click');
                $(event.target).click(removeFromFavorites);
            } else {
                $(event.target).removeClass('active');
            }
         });  
    }
    
    /**
     * Ajouter aux favoris
     * 
     * @param {type} event
     * @returns {undefined}
     */
    function removeFromFavorites(event) {

        // Stop l'évènement
        event.preventDefault();
        
        $(event.target).removeClass('active');
        
        // Requête AJAX
        $.ajax({
            url: sub_url_base + 'ajax-request/users/removeFromFavorites',
            data: {url: $(event.target).attr('name').substring(13)},
            type: 'post'
         }).done(function(res) {
            res = jQuery.parseJSON(res);

            if (res.result == true) {
                $(event.target).unbind('click');
                $(event.target).click(addToFavorites);

                if (typeof favorites !== 'undefined' && favorites == true) {
                    $('li[data-slug="'+res.content.url+'"]').each(function(index, element) {
                        $(element).fadeOut(500);
                    });
    
                }
                
            } else {
                $(event.target).addClass('active');
            }
         });  
    }
    
    /**
     * Ajouter aux favoris
     */
    $('a[name^="favorite-add-"]').each(function(index, element) {
        $(element).click(addToFavorites);
    });
    
    /**
     * Ajouter aux favoris
     */
    $('a[name^="favorite-rmv-"]').each(function(index, element) {
        $(element).click(removeFromFavorites);
    });
    
});

/*
$(document).ready(function() {

    createDropDown();
    
    $(".dropdown dt a").click(function() {
        $(".dropdown dd ul").toggle();
    });

    $(document).bind('click', function(e) {
        var $clicked = $(e.target);
        if (! $clicked.parents().hasClass("dropdown"))
            $(".dropdown dd ul").hide();
    });
                
    $(".dropdown dd ul li a").click(function() {
        var text = $(this).html();
        $(".dropdown dt a").html(text);
        $(".dropdown dd ul").hide();
        
        var source = $("#source");
        source.val($(this).find("span.value").html())
    });
});

function createDropDown(){

    var source = $("#source");
    var selected = source.find("option[selected]");
    var options = $("option", source);
    
    $("#home-input").after('<dl id="target" class="dropdown"></dl>')
    $("#target").append('<dt><a href="javascript:;">' + selected.text() + 
        '<span class="value">' + selected.val() + 
        '</span></a></dt>')
    $("#target").append('<dd><ul></ul></dd>')

    options.each(function(){
        $("#target dd ul").append('<li><a href="javascript:;">' + 
            $(this).text() + '<span class="value">' + 
            $(this).val() + '</span></a></li>');
    });

    source.hide();
}*/