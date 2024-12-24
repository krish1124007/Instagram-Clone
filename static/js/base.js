const bd = document.getElementById("inner-Container");
const form = document.getElementById('post-form');

const moodchanger = document.getElementById("mc");
const Ispost = () => {
    if (form.style.display === 'none' || form.style.display === '') {
        // Show the form
        // form.style.display = 'block';
        gsap.to(form ,{
            display:'block'
        })
        gsap.to(bd ,{
            opacity:0.4,
            duration:1,
            ease:"elastic"
        })
        
        
    } else {
        // Hide the form
        form.style.display = 'none';
        bd.style.opacity = 1;
        gsap.to(form, {
            display:"none",

        })
        gsap.to(bd , {
            opacity:1
        })
    }
}




// Get reference to body element
const body = document.body;

// Retrieve the stored class name from localStorage, or default to 'simple-body' if not found
let storedClassName = localStorage.getItem('bodyclassname') || 'simple-body';

// Apply the stored or default class name to the body
body.className = storedClassName;

// Functions to change the body class and update localStorage
const sigma = () => {
    body.className = 'sigma-body';
    body.style.color = 'white'
    
      localStorage.setItem('bodyclassname', body.className);
}

const love = () => {
    body.className = 'love-body';
    localStorage.setItem('bodyclassname', body.className);
}

const dark = () => {
    body.className = 'dark-body';
    localStorage.setItem('bodyclassname', body.className);
}

const danger = () => {
    body.className = 'danger-body';
    localStorage.setItem('bodyclassname', body.className);
}

const simple = () => {
    body.className = 'simple-body';
    localStorage.setItem('bodyclassname', body.className);
}

const ModeChnage = () => {
    if (moodchanger.style.display === "none" || moodchanger.style.display === '') {
        moodchanger.style.display = "flex";
        bd.style.opacity = 0.2;
    } else {
        moodchanger.style.display = "none";
        bd.style.opacity = 1;
    }
}
