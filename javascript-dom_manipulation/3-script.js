// Select the header element using querySelector and by id 
const headerElement = document.querySelector('header');
const toggleHeader = document.getElementById('toggle_header');

function changeColor() {
    // toggles the text color of the header element
    if (headerElement.classList.contains("red")) {
      headerElement.classList.remove("red");
      headerElement.classList.add("green");
    } else if (headerElement.classList.contains("green")) {
      headerElement.classList.remove("green");
      headerElement.classList.add("red");
    }
  }
  toggleHeader.addEventListener("click", changeColor);