// fetch api data
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const character = document.getElementById('character');

fetch(url)
  .then(response => response.json())
  .then(data => {
    character.textContent = data.name;
  });