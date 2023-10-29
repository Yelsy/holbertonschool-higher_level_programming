$.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    dataType: 'json',
    success: function(data) {
      $('#hello').text(data.hello);
    },
    error: function() {
      // Handle any errors here
      $('#hello').text('Error fetching translation');
    }
  });
