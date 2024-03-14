const button = document.querySelector('button');

button.addEventListener('click', function() {
    button.style.transform = 'scale(0.95)';
    setTimeout(() => {
        button.style.transform = 'scale(1)';
    }, 200);
});
