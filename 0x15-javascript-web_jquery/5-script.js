// adds a list element to a list upon click
$('div#add_item').on('click', function () {
  $('ul.my_list').append('<li>Item</li>');
});
