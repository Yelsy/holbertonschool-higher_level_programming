//featch api data 
const helloItem = document.getElementById("hello");
const url = "https://hellosalut.stefanbohacek.dev/?lang=fr";

// Fetch the translation and update the "hello" element
fetch(url)
.then((response) => response.json())
.then((data) => {
  const translation = data.hello;
  // Update the content of the "hello" element with the translation
  helloItem.textContent = translation;
})
