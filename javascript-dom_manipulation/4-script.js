// select the node 
const addItem = document.getElementById('add_item');
const my_list = document.querySelector('.my_list');

addItem.addEventListener('click', ()=>{
    /*creates a new list item with the text "Item" 
    and appends it to the existing unordered list on the page */
    let li = document.createElement('LI');
    li.textContent = 'Item';
    my_list.appendChild(li);
});