// Send an AJAX request to the specified URL using the jQuery $.ajax method
$.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    dataType: 'json',
    success: function(data) {
      // Display the translation in the div with the ID hello
      $('#hello').text(data.hello);
    },
    error: function() {
      // Handle any errors here
      $('#hello').text('Error fetching translation');
    }
  });
