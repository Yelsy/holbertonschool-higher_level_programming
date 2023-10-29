// Send an AJAX GET request to the specified URL
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
  // Iterate through the movies and add their titles to the list
  $.each(data.results, function(index, movie) {
    const listItem = $('<li>').text(movie.title);
    $('#list_movies').append(listItem);
  });
});
