function main () {

    var community = document.getElementById("content-community"); //-- Bloque de contenido de comunidad de la página
    var text_community = community.innerHTML; //-- Texto que contiene el bloque
    community.innerHTML = ""; //-- Lo ocultamos para que al principio no se muestre
    console.log(text_community);
    var boton_comunidad = document.getElementById("mostrar-comunidad"); //-- Botón para desplegar u ocultar los datos

    //-- Variables del bloque de seguridad
    var security = document.getElementById("content-security");
    var text_security = security.innerHTML;
    security.innerHTML = "";
    console.log(text_security);
    var boton_seguridad = document.getElementById("mostrar-seguridad");

    

    var mostrando_com = false; //-- Booleano para controlar si se están mostrando los datos de comunidad
    var mostrando_sec = false; //-- Booleano para controlar si se están mostrando los datos de seguridad

    boton_comunidad.onclick = () => {
        if (mostrando_com) { //-- Si se están mostrando los datos...
            community.innerHTML = ""; //-- ...los ocultamos
            boton_comunidad.innerHTML = "Mostrar pestaña de comunidad";
            mostrando_com = false; //-- Cambiamos el booleano porque ya no lo estamos mostrando
        } else { //-- Si no se están mostrando...
            community.innerHTML = text_community; //-- ...los desplegamos
            boton_comunidad.innerHTML = "Ocultar pestaña de comunidad";
            mostrando_com = true; //-- Cambiamos el booleano porque ahora lo estamos mostrando
        }
    }

    boton_seguridad.onclick = () => {
        if (mostrando_sec) { //-- Si se están mostrando los datos...
            security.innerHTML = ""; //-- ...los ocultamos
            boton_seguridad.innerHTML = "Mostrar pestaña de seguridad";
            mostrando_sec = false; //-- Cambiamos el booleano porque ya no lo estamos mostrando
        } else { //-- Si no se están mostrando...
            security.innerHTML = text_security; //-- ...los desplegamos
            boton_seguridad.innerHTML = "Ocultar pestaña de seguridad";
            mostrando_sec = true; //-- Cambiamos el booleano porque ahora lo estamos mostrando
        }
    }
}