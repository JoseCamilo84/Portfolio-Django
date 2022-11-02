const hamburg = document.getElementById('hamburg');
const nav_bar = document.getElementById('nav-bar');

hamburg.addEventListener('click', () => {
    nav_bar.classList.toggle('nav-bar-show');
});