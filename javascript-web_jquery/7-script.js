// Send an AJAX GET request to the specified URL
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function(data) {
  $('#character').text(data.name);
});
