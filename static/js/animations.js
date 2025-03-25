// animations.js

// Efecto de hover en los productos
const productItems = document.querySelectorAll('.product-item');
productItems.forEach(item => {
item.addEventListener('mouseenter', () => {
item.style.transform = 'scale(1.05)';
item.style.transition = 'transform 0.3s ease';
});
item.addEventListener('mouseleave', () => {
item.style.transform = 'scale(1)';
});
});

// Animación para el logo
const logo = document.querySelector('.logo-img');
logo.addEventListener('mouseenter', () => {
logo.style.animation = 'float 3s ease-in-out infinite';
});
logo.addEventListener('mouseleave', () => {
logo.style.animation = 'none';
});

// Animación para el título
const title = document.querySelector('.title');
title.addEventListener('mouseenter', () => {
title.style.color = '#ffeb3b';
title.style.transition = 'color 0.3s ease';
});
title.addEventListener('mouseleave', () => {
title.style.color = 'white';
});