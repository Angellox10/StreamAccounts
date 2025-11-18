/* ============================================
   STREAMACCOUNTS - MAIN.JS
   Scripts principales para la plataforma
   ============================================ */

document.addEventListener('DOMContentLoaded', function() {
    
    // Animación suave al hacer scroll
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Animación de entrada para las cards
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '0';
                entry.target.style.transform = 'translateY(20px)';
                
                setTimeout(() => {
                    entry.target.style.transition = 'all 0.6s ease';
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, 100);
                
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observar todas las product cards
    document.querySelectorAll('.product-card').forEach(card => {
        observer.observe(card);
    });

    // Contador animado para el carrito
    const cartButtons = document.querySelectorAll('.btn-add-cart');
    cartButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            // Animación de pulso al agregar al carrito
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
        });
    });

    // Tooltip para badges de stock
    const stockBadges = document.querySelectorAll('.stock-badge');
    stockBadges.forEach(badge => {
        badge.setAttribute('title', badge.textContent.includes('Disponible') 
            ? 'Producto disponible para compra inmediata' 
            : 'Producto temporalmente agotado');
    });

    // Formateo de precios con separadores de miles
    const priceTags = document.querySelectorAll('.price-tag, .price-display');
    priceTags.forEach(price => {
        const value = price.textContent.replace(/[^0-9]/g, '');
        if (value) {
            const formatted = new Intl.NumberFormat('es-CO', {
                style: 'currency',
                currency: 'COP',
                minimumFractionDigits: 0
            }).format(value);
            price.textContent = formatted;
        }
    });

    // Efecto de carga para imágenes
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                imageObserver.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));

    // Confirmación antes de agregar al carrito (opcional)
    const addToCartLinks = document.querySelectorAll('a[href*="agregar_al_carrito"]');
    addToCartLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const productName = this.closest('.product-card')?.querySelector('.product-title')?.textContent;
            if (productName) {
                console.log(`Agregando al carrito: ${productName}`);
            }
        });
    });

    // Búsqueda en tiempo real (si existe input de búsqueda)
    const searchInput = document.querySelector('input[name="q"]');
    if (searchInput) {
        let searchTimeout;
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                const query = this.value.toLowerCase();
                console.log('Buscando:', query);
                // Aquí se puede implementar búsqueda AJAX
            }, 300);
        });
    }

    // Animación del navbar al hacer scroll
    let lastScroll = 0;
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll <= 0) {
            navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.3)';
        } else {
            navbar.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.5)';
        }
        
        lastScroll = currentScroll;
    });

    // Toggle para mostrar/ocultar descripción completa en mobile
    const toggleButtons = document.querySelectorAll('[data-toggle-description]');
    toggleButtons.forEach(button => {
        button.addEventListener('click', function() {
            const description = this.previousElementSibling;
            description.classList.toggle('expanded');
            this.textContent = description.classList.contains('expanded') 
                ? 'Ver menos' 
                : 'Ver más';
        });
    });

    console.log('🎬 StreamAccounts - Scripts cargados correctamente');
});

// Función para actualizar contador del carrito (si existe)
function updateCartCount() {
    // Esta función se puede llamar después de agregar items al carrito
    const cartLink = document.querySelector('a[href*="ver_carrito"]');
    if (cartLink) {
        // Aquí se puede hacer una petición AJAX para obtener el número de items
        console.log('Actualizando contador del carrito...');
    }
}

// Exportar funciones útiles
window.StreamAccounts = {
    updateCartCount: updateCartCount
};
