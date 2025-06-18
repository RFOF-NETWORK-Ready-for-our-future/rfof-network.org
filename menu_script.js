document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('navLinks');

    // Toggle for the global hamburger menu
    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }

    // Handle clicks outside the global dropdown to close it
    document.addEventListener('click', (event) => {
        if (navLinks && !navLinks.contains(event.target) && !hamburger.contains(event.target)) {
            navLinks.classList.remove('active');
        }
    });

    // --- Specific logic for the new RFOF-NETWORK.org dropdown ---
    const rfofDropdownButton = document.querySelector('.rfof-dropdown-button');
    const rfofDropdownContent = document.querySelector('.rfof-dropdown-content');

    if (rfofDropdownButton && rfofDropdownContent) {
        // Toggle the RFOF dropdown visibility on button click
        rfofDropdownButton.addEventListener('click', (event) => {
            event.stopPropagation(); // Prevent the click from immediately closing the dropdown via document listener
            rfofDropdownContent.style.display = rfofDropdownContent.style.display === 'block' ? 'none' : 'block';
        });

        // Close the RFOF dropdown if clicked outside
        document.addEventListener('click', (event) => {
            if (!rfofDropdownContent.contains(event.target) && !rfofDropdownButton.contains(event.target)) {
                rfofDropdownContent.style.display = 'none';
            }
        });

        // Close the RFOF dropdown when a link inside it is clicked
        rfofDropdownContent.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                rfofDropdownContent.style.display = 'none';
                // Optional: For smooth scrolling to anchor links
                const href = link.getAttribute('href');
                if (href && href.startsWith('#')) {
                    const targetElement = document.querySelector(href);
                    if (targetElement) {
                        targetElement.scrollIntoView({ behavior: 'smooth' });
                    }
                }
            });
        });
    }
});
