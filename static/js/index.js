const footerP = document.querySelector('.footer-content');
const newDate = new Date();

footerP.innerHTML += ` | ${newDate.getFullYear()}`;
