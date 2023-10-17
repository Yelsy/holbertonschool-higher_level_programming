// Select the header element using querySelector and by id 
const headerElement = document.querySelector('header');
const redHeaderElement= document.getElementById('red_header');

function changeColor(){
    headerElement.classList.add('red');
}
//  change the text color of the header element to red.
redHeaderElement.addEventListener('click', changeColor);