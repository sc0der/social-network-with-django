
    $(document).ready(function(){
      $('.collapsible').collapsible();
    });
    $(document).ready(function(){
      $('.sidenav').sidenav();
    });

    $('.toggler').on('click', function() {
      $('.ui.labeled.icon.sidebar').sidebar('toggle');
  });
  $(document).ready(function(){
 
    $(window).scroll(function(){
    if ($(this).scrollTop() > 100) {
    $('.scrollup').fadeIn();
    } else {
    $('.scrollup').fadeOut();
    }
    });
     
    $('.scrollup').click(function(){
    $("html, body").animate({ scrollTop: 0 }, 600);
    return false;
    });
    $("#formButton").click(function() {
    $("#replay").toggle(500);
    });
  });
  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.fixed-action-btn');
    var instances = M.FloatingActionButton.init(elems, {
      direction: 'left',
      hoverEnabled: false
    });
  });
  grecaptcha.ready(function() {
    $('#contactform').submit(function(e){
        var form = this;
        // 5
        e.preventDefault()
        grecaptcha.execute('reCAPTCHA_site_key', {action: 'contactform'}).then(function(token) {
            // 6
            $('#recaptcha').val(token)
            // 7
            form.submit()
        });
    });

});