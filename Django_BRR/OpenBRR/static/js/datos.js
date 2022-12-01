function main () {

    var content = document.getElementById("content"); //-- Bloque de contenido de la página
    var text_content = content.innerHTML; //-- Texto que contiene el bloque
    content.innerHTML = ""; //-- Lo ocultamos para que al principio no se muestre
    console.log(text_content);

    var boton_prueba = document.getElementById("mostrar"); //-- Botón para desplegar u ocultar los datos

    var mostrando = false; //-- Booleano para controlar si se están mostrando los datos

    boton_prueba.onclick = () => {
        if (mostrando) { //-- Si se están mostrando los datos...
            content.innerHTML = ""; //-- ...los ocultamos
            mostrando = false; //-- Cambiamos el booleano porque ya no lo estamos mostrando
        } else { //-- Si no se están mostrando...
            content.innerHTML = text_content; //-- ...los desplegamos
            mostrando = true; //-- Cambiamos el booleano porque ahora lo estamos mostrando
        }
    }
}