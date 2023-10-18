// select the element header 
const update_header = document.getElementById('update_header');
const header = document.querySelector('header');

update_header.addEventListener('click', () =>{
    header.textContent = "New Header!!!";
});
