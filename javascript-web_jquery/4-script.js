$(document).ready(function() {
    // Add a click event handler to the DIV with ID 'toggle_header'
    $('#toggle_header').click(function() {
      // Select the <header> element 
      const header = $('header');
  
      if (header.hasClass('red')) {
        // If it has the 'red' class, toggle to 'green'
        header.removeClass('red');
        header.addClass('green');
      } else {
        // If it has the 'green' class or no class, toggle to 'red'
        header.removeClass('green');
        header.addClass('red');
      }
    });
  });
  