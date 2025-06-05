const addItem = document.getElementById('add_item');

addItem.addEventListener('click', function () {
  const list = document.querySelector('ul.my_list');
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  list.appendChild(newItem);
});
