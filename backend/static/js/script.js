$(function() {
    $('.spinner').each(function() {
      var el  = $(this);
      var add = $('.spinner-add');
      var sub = $('.spinner-sub');
  
      // substract
      el.parent().on('click', '.spinner-sub', function() {
        if (el.val() > parseInt(el.attr('min'))) {
          el.val(function(i, oldval) {
            return --oldval;
          });
        }
        // disabled
        if (el.val() == parseInt(el.attr('min'))) {
          el.prev(sub).addClass('disabled');
        }
        if (el.val() < parseInt(el.attr('max'))) {
          el.next(add).removeClass('disabled');
        }
      });
  
      // increment
      el.parent().on('click', '.spinner-add', function() {
        if (el.val() < parseInt(el.attr('max'))) {
          el.val(function(i, oldval) {
            return ++oldval;
          });
        }
        // disabled
        if (el.val() > parseInt(el.attr('min'))) {
          el.prev(sub).removeClass('disabled');
        }
        if (el.val() == parseInt(el.attr('max'))) {
          el.next(add).addClass('disabled');
        }
      });
    });
  });