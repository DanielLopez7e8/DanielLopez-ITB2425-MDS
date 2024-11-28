document.addEventListener("DOMContentLoaded", function() {
    // Detectar cambios de visibilidad
    document.addEventListener("visibilitychange", function() {
        if (document.hidden) {
            // Cambiar el título cuando la página no es visible
            document.title = "¡No te vayas!:(";
        } else {
            // Restaurar el título original cuando la página vuelve a ser visible
            document.title = "HOME";
        }
    });
});
