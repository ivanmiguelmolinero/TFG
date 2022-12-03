function main () {

    var content = document.getElementById("content"); //-- Bloque de contenido de la página
    var text_content = content.innerHTML; //-- Texto que contiene el bloque
    content.innerHTML = ""; //-- Lo ocultamos para que al principio no se muestre
    console.log(text_content);

    var boton_comunidad = document.getElementById("mostrar"); //-- Botón para desplegar u ocultar los datos

    var mostrando = false; //-- Booleano para controlar si se están mostrando los datos

    boton_comunidad.onclick = () => {
        if (mostrando) { //-- Si se están mostrando los datos...
            content.innerHTML = ""; //-- ...los ocultamos
            boton_comunidad.innerHTML = "Mostrar pestaña de comunidad";
            mostrando = false; //-- Cambiamos el booleano porque ya no lo estamos mostrando
        } else { //-- Si no se están mostrando...
            content.innerHTML = text_content; //-- ...los desplegamos
            boton_comunidad.innerHTML = "Ocultar pestaña de comunidad";
            mostrando = true; //-- Cambiamos el booleano porque ahora lo estamos mostrando
        }
    }
}