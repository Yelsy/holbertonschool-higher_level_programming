// fetch data 
const movieList = document.getElementById("list_movies");
const url = "https://swapi-api.hbtn.io/api/films/?format=json";

// Fetch the data from the API and process it
fetch(url)
  .then(response => response.json())
  .then(data => {
    // Extract the list of movies from the API response
    const movies = data.results;

    // Loop through the movies and add them to the <ul> element
    movies.forEach(movie => {
        const listItem = document.createElement("LI");
        listItem.textContent = movie.title;
        movieList.appendChild(listItem);
      });
  });