const toggleHeader = document.getElementById('toggle_header');

toggleHeader.addEventListener('click', function () {
  const header = document.querySelector('header');

  if (header.classList.contains('red')) {
    header.classList.replace('red', 'green');
  } else {
    header.classList.replace('green', 'red');
  }
});
