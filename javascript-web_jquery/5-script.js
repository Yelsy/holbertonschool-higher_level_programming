$(document).ready(function() {
    $('#add_item').click(function() {
      // Create a new li element
      const newItem = $('<li>Item</li');
      // Append the new li element to the ul with the class my_list
      $('ul.my_list').append(newItem);
    });
  });
  