function main () {

    var community = document.getElementById("content-community"); //-- Bloque de contenido de comunidad de la página
    var text_community = community.innerHTML; //-- Texto que contiene el bloque
    community.innerHTML = ""; //-- Lo ocultamos para que al principio no se muestre
    var boton_comunidad = document.getElementById("mostrar-comunidad"); //-- Botón para desplegar u ocultar los datos

    //-- Variables del bloque de seguridad
    var security = document.getElementById("content-security");
    var text_security = security.innerHTML;
    security.innerHTML = "";
    var boton_seguridad = document.getElementById("mostrar-seguridad");

    //-- Variables del bloque de seguridad
    var funcionality = document.getElementById("content-funcionality");
    var text_funcionality = funcionality.innerHTML;
    funcionality.innerHTML = "";
    var boton_funcionalidad = document.getElementById("mostrar-funcionalidad");

    //-- Variables del bloque de soporte
    var support = document.getElementById("content-support");
    var text_support = support.innerHTML;
    support.innerHTML = "";
    var boton_soporte = document.getElementById("mostrar-soporte");

    //-- Variables del bloque de calidad
    var quality = document.getElementById("content-quality");
    var text_quality = quality.innerHTML;
    quality.innerHTML = "";
    var boton_calidad = document.getElementById("mostrar-calidad");

    //-- Variables del bloque de usabilidad
    var usability = document.getElementById("content-usability");
    var text_usability = usability.innerHTML;
    usability.innerHTML = "";
    var boton_usabilidad = document.getElementById("mostrar-usabilidad");

    //-- Variables del bloque de adopción
    var adoption = document.getElementById("content-adoption");
    var text_adoption = adoption.innerHTML;
    adoption.innerHTML = "";
    console.log(text_adoption);
    var boton_adoption = document.getElementById("mostrar-adopcion");


    

    var mostrando_com = false; //-- Booleano para controlar si se están mostrando los datos de comunidad
    var mostrando_sec = false; //-- Booleano para controlar si se están mostrando los datos de seguridad
    var mostrando_func = false; //-- Booleano para controlar si se están mostrando los datos de funcionalidad
    var mostrando_supp = false; //-- Booleano para controlar si se están mostrando los datos de soporte
    var mostrando_qual = false; //-- Booleano para controlar si se están mostrando los datos de calidad
    var mostrando_usab = false; //-- Booleano para controlar si se están mostrando los datos de uabilidad
    var mostrando_adop = false; //-- Booleano para controlar si se están mostrando los datos de adopción

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

    boton_funcionalidad.onclick = () => {
        if (mostrando_func) { //-- Si se están mostrando los datos...
            funcionality.innerHTML = ""; //-- ...los ocultamos
            boton_funcionalidad.innerHTML = "Mostrar pestaña de funcionalidad";
            mostrando_func = false; //-- Cambiamos el booleano porque ya no lo estamos mostrando
        } else { //-- Si no se están mostrando...
            funcionality.innerHTML = text_funcionality; //-- ...los desplegamos
            boton_funcionalidad.innerHTML = "Ocultar pestaña de funcionaldidad";
            mostrando_func = true; //-- Cambiamos el booleano porque ahora lo estamos mostrando
        }
    }

    boton_soporte.onclick = () => {
        if (mostrando_supp) { //-- Si se están mostrando los datos...
            support.innerHTML = ""; //-- ...los ocultamos
            boton_soporte.innerHTML = "Mostrar pestaña de soporte";
            mostrando_supp = false; //-- Cambiamos el booleano porque ya no lo estamos mostrando
        } else { //-- Si no se están mostrando...
            support.innerHTML = text_support; //-- ...los desplegamos
            boton_soporte.innerHTML = "Ocultar pestaña de soporte";
            mostrando_supp = true; //-- Cambiamos el booleano porque ahora lo estamos mostrando
        }
    }

    boton_calidad.onclick = () => {
        if (mostrando_qual) { //-- Si se están mostrando los datos...
            quality.innerHTML = ""; //-- ...los ocultamos
            boton_calidad.innerHTML = "Mostrar pestaña de calidad";
            mostrando_qual = false; //-- Cambiamos el booleano porque ya no lo estamos mostrando
        } else { //-- Si no se están mostrando...
            quality.innerHTML = text_quality; //-- ...los desplegamos
            boton_calidad.innerHTML = "Ocultar pestaña de calidad";
            mostrando_qual = true; //-- Cambiamos el booleano porque ahora lo estamos mostrando
        }
    }

    boton_usabilidad.onclick = () => {
        if (mostrando_usab) { //-- Si se están mostrando los datos...
            usability.innerHTML = ""; //-- ...los ocultamos
            boton_usabilidad.innerHTML = "Mostrar pestaña de usabilidad";
            mostrando_usab = false; //-- Cambiamos el booleano porque ya no lo estamos mostrando
        } else { //-- Si no se están mostrando...
            usability.innerHTML = text_usability; //-- ...los desplegamos
            boton_usabilidad.innerHTML = "Ocultar pestaña de usabilidad";
            mostrando_usab = true; //-- Cambiamos el booleano porque ahora lo estamos mostrando
        }
    }

    boton_adoption.onclick = () => {
        if (mostrando_adop) { //-- Si se están mostrando los datos...
            adoption.innerHTML = ""; //-- ...los ocultamos
            boton_adoption.innerHTML = "Mostrar pestaña de adopción";
            mostrando_adop = false; //-- Cambiamos el booleano porque ya no lo estamos mostrando
        } else { //-- Si no se están mostrando...
            adoption.innerHTML = text_adoption; //-- ...los desplegamos
            boton_adoption.innerHTML = "Ocultar pestaña de adopción";
            mostrando_adop = true; //-- Cambiamos el booleano porque ahora lo estamos mostrando
        }
    }
}