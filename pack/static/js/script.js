const navBtn = document.getElementById('nav-btn');
const cancelBtn = document.getElementById('cancel-btn');
const sideNav = document.getElementById('sidenav');
const modal = document.getElementById('modal');

navBtn.addEventListener("click", function(){
    sideNav.classList.add('show');
    modal.classList.add('showModal');
});

cancelBtn.addEventListener('click', function(){
    sideNav.classList.remove('show');
    modal.classList.remove('showModal');
});

window.addEventListener('click', function(event){
    if(event.target === modal){
        sideNav.classList.remove('show');
        modal.classList.remove('showModal');
    }
});

// Navigation and Menu functionality
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Sticky navigation on scroll
    window.addEventListener('scroll', function() {
        const header = document.querySelector('.head-top');
        header.classList.toggle('sticky', window.scrollY > 0);
    });

    // Mobile menu toggle
    const menuBtn = document.querySelector('.menu-toggle');
    const navbar = document.querySelector('.navbar');
    let isMenuOpen = false;

    if (menuBtn) {
        menuBtn.addEventListener('click', () => {
            isMenuOpen = !isMenuOpen;
            navbar.classList.toggle('active');
            menuBtn.classList.toggle('active');
            menuBtn.setAttribute('aria-expanded', isMenuOpen);
        });
    }

    // Search functionality
    const searchBtn = document.querySelector('.head-btn');
    if (searchBtn) {
        searchBtn.addEventListener('click', function() {
            // Add your search functionality here
            console.log('Search button clicked');
        });
    }

    // Room booking buttons
});

// Image loading and animation
document.addEventListener('DOMContentLoaded', function() {
    // Lazy loading for images
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                if (img.dataset.src) {
                    img.src = img.dataset.src;
                    img.classList.add('loaded');
                    img.removeAttribute('data-src');
                    observer.unobserve(img);
                }
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '50px'
    });

    // Observe all images with data-src attribute
    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });

    // Fallback for browsers that don't support IntersectionObserver
    if (!('IntersectionObserver' in window)) {
        document.querySelectorAll('img[data-src]').forEach(img => {
            img.src = img.dataset.src;
            img.classList.add('loaded');
            img.removeAttribute('data-src');
        });
    }
});

// Add error handling for images
document.querySelectorAll('img').forEach(img => {
    img.addEventListener('error', function() {
        this.src = '{{ url_for('static', filename='images/placeholder.jpg') }}';
        this.alt = 'Image not available';
    });
});

// Logo scroll effect
window.addEventListener('scroll', function() {
    const header = document.querySelector('.head-top');
    if (window.scrollY > 50) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});