// script.js

// Bandera para saber si el usuario está cerrando la ventana
let isAttemptingToClose = false;

// Detectamos si el usuario hace clic en enlaces internos
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(event) {
        // Desactivar el mensaje de confirmación si el usuario navega internamente
        isAttemptingToClose = false;
    });
});

// Detectamos cuando el usuario intenta cerrar la ventana o pestaña
window.addEventListener('beforeunload', function(event) {
    // Solo mostrar el mensaje si está intentando cerrar la ventana y no navega entre secciones internas
    if (isAttemptingToClose) {
        const message = "¿Estás seguro de que deseas salir? Te perderás proyectos MUY interesantes!";
        
        // Esto es necesario para los navegadores modernos
        event.returnValue = message;  // Esto activa el mensaje en la mayoría de los navegadores
        return message;  // Para compatibilidad con navegadores más antiguos
    }
});

// Marca la bandera cuando el usuario realmente está cerrando la ventana o pestaña
window.addEventListener('unload', function() {
    isAttemptingToClose = true;
});

// Cuando la página se recarga o se carga por completo, aseguramos que la bandera esté resetada
window.addEventListener('load', function() {
    // Restablecemos la bandera a false cuando la página se recarga
    isAttemptingToClose = false;
});
