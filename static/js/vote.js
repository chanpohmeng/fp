$(Document).ready(function() {
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
  
  var csrftoken = getCookie('csrftoken');
  
  function vote(subID) {
    $.ajax({
      type:"POST",
      url: "/vote/",
      data: {submission: "submissionID"},
      success: function() {
        $("#upv-" + subID).hide();
    },
      headers: {
        'X-CSRFToken': csrftoken
      }
    });
    return false;
  }
  
  $('a.vote').click(function() {
    var subID = this.subID
    return vote(subID);
  })

});