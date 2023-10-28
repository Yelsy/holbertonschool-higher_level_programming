// wait for the document to be ready
$(document).ready(function() {
    // Add a click event handler
    $('#red_header').click(function() {
        // select the header element 
        $('header').css('color', '#FF0000');
    });
});
