// Get a reference to the button with the ID "red_header"
const redHeaderElement = document.getElementById('red_header');

//Add a click event listener to the "red_header" element
redHeaderElement.addEventListener('click', function(){
    // Select the header element
    const headerElement = document.querySelector('header');
    headerElement.style.color = '#FF0000';
})