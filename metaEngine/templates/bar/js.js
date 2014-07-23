$( document ).ready(function() {

// Artificial custom focus action for Search Bar
var searchInput = $(".nav-search-container .search-input"),
    selectInput = $("#type");

// Focus if we click
searchInput.focus(function(){
    $(this).parent().addClass('focused');
});

searchInput.blur(function(){
   window.setTimeout(blurTester, 100);
});
selectInput.blur(function(){
    window.setTimeout(blurTester, 100);
});

function blurTester() {
  if ($(searchInput).is(":focus") ||  $(selectInput).is(":focus") ){
  }
  else if ($(searchInput).val()) {

  }
  else {
    $('.nav-search-container').removeClass('focused');
  }
}
  // Show submit on input type
  searchInput.keypress(function(){
    if($(this).val() < 1){
      $(this).parent().addClass('show-submit');
    }
  });
  
});
