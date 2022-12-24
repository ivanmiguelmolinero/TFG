function main () {

    //-- Variables del bloque de comunidad
    var community = document.getElementById("content-community"); //-- Bloque de contenido de comunidad de la página
    var text_community = community.innerHTML; //-- Texto que contiene el bloque
    var boton_comunidad = document.getElementById("mostrar-comunidad"); //-- Botón para desplegar u ocultar los datos
    //var datos_commits = document.getElementById("commits");
    community.innerHTML = ""; //-- Lo ocultamos para que al principio no se muestre
    

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
    var boton_adoption = document.getElementById("mostrar-adopcion");
    

    var mostrando_com = false; //-- Booleano para controlar si se están mostrando los datos de comunidad
    var mostrando_sec = false; //-- Booleano para controlar si se están mostrando los datos de seguridad
    var mostrando_func = false; //-- Booleano para controlar si se están mostrando los datos de funcionalidad
    var mostrando_supp = false; //-- Booleano para controlar si se están mostrando los datos de soporte
    var mostrando_qual = false; //-- Booleano para controlar si se están mostrando los datos de calidad
    var mostrando_usab = false; //-- Booleano para controlar si se están mostrando los datos de uabilidad
    var mostrando_adop = false; //-- Booleano para controlar si se están mostrando los datos de adopción

    //-- Botones de las pestañas
    boton_comunidad.onclick = () => {
        if (mostrando_com) { //-- Si se están mostrando los datos...
            console.log(community.innerHTML)
            text_community = community.innerHTML; //-- Guardamos los cambios hechos por el usuario
            community.innerHTML = ""; //-- ...los ocultamos
            boton_comunidad.innerHTML = "Mostrar pestaña de comunidad";
            mostrando_com = false; //-- Cambiamos el booleano porque ya no lo estamos mostrando
        } else { //-- Si no se están mostrando...
            community.innerHTML = text_community; //-- ...los desplegamos
            boton_comunidad.innerHTML = "Ocultar pestaña de comunidad";
            //var valor_commits = document.getElementById("valor-commits");
            //console.log(valor_commits.getAttribute('max'));
            mostrando_com = true; //-- Cambiamos el booleano porque ahora lo estamos mostrando
        }
    }

    boton_seguridad.onclick = () => {
        if (mostrando_sec) { //-- Si se están mostrando los datos...
            text_security = security.innerHTML; //-- Guardamos los cambios hechos por el usuario
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

//-- Controla que el usuario no pueda meter valores que sumen más del 100% en la pestaña de comunidad
function edit_max_value_community(value) {
    console.log("edito")
    element_to_edit = 'valor-' + value;
    console.log(element_to_edit);
    //-- Obtenemos cada elemento valor
    var commits = document.getElementById("valor-commits");
    var forks = document.getElementById("valor-forks");
    var suscriptores = document.getElementById("valor-suscriptores");
    var org = document.getElementById("valor-organización");
    var actualizacion = document.getElementById("valor-actualización");
    community_list = [commits, forks, suscriptores, org, actualizacion]

    console.log(value)
    //-- Obtenememos la suma de los valores del resto de elementos
    //suma =  parseFloat(forks.value) + parseFloat(suscriptores.value) + parseFloat(org.value) + parseFloat(actualizacion.value);
    //-- Asignamos la ponderación máxima como la resta del 100% menos la suma anterior
    new_max = (100 - get_suma(community_list, element_to_edit));
    set_max_attribute(element_to_edit, new_max);
    //commits.setAttribute('max', String(new_max));
    //console.log(commits.getAttribute('max'))
    save_input_community('valor-' + value)
}

//-- Controla que el usuario no pueda meter valores que sumen más del 100% en la pestaña de seguridad
function edit_max_value_security(value) {
    console.log("edito")
    element_to_edit = 'valor-' + value;
    console.log(element_to_edit);
    //-- Obtenemos cada elemento valor
    var licencia = document.getElementById("valor-licencia");
    var viewers = document.getElementById("valor-viewers");
    var problemas = document.getElementById("valor-problemas");
    var vulnerabilidad = document.getElementById("valor-vulnerabilidad");
    security_list = [licencia, viewers, problemas, vulnerabilidad];

    //-- Asignamos la ponderación máxima como la resta del 100% menos la suma anterior
    new_max = (100 - get_suma(security_list, element_to_edit));
    set_max_attribute(element_to_edit, new_max);
    save_input_security(element_to_edit);
}

//-- Guarda los cambios que haga el usuario en la pestaña de comunidad
function save_input_community(input) {
    if (input == 'organización-sí') {
        console.log(document.getElementById(input).checked);
        document.getElementById(input).setAttribute('checked', '');
        document.getElementById('organización-no').removeAttribute('checked');
    } else if (input == 'organización-no') {
        document.getElementById(input).setAttribute('checked', '');
        document.getElementById('organización-sí').removeAttribute('checked');
    } else {
        document.getElementById(input).setAttribute("value",
            document.getElementById(input).value);
    }
    var community = document.getElementById('content-community')
    text_community = community.innerHTML;
}

//-- Guarda los cambios que haga el usuario en la pestaña de seguridad
function save_input_security(input) {
    if (input == 'licencia-sí') {
        document.getElementById(input).setAttribute('checked', '');
        document.getElementById('licencia-no').removeAttribute('checked');
    } else if (input == 'licencia-no') {
        document.getElementById(input).setAttribute('checked', '');
        document.getElementById('licencia-sí').removeAttribute('checked');
    } else if (input == 'problemas-sí') {
        document.getElementById(input).setAttribute('checked', '');
        document.getElementById('problemas-no').removeAttribute('checked');
    } else if (input == 'problemas-no') {
        document.getElementById(input).setAttribute('checked', '');
        document.getElementById('problemas-sí').removeAttribute('checked');
    } else if (input == 'vulnerabilidad-sí') {
        document.getElementById(input).setAttribute('checked', '');
        document.getElementById('vulnerabilidad-no').removeAttribute('checked');
    } else if (input == 'vulnerabilidad-no') {
        document.getElementById(input).setAttribute('checked', '');
        document.getElementById('vulnerabilidad-sí').removeAttribute('checked');
    } else {
        document.getElementById(input).setAttribute("value",
            document.getElementById(input).value);
    }
    var security = document.getElementById('content-security');
    text_security = security.innerHTML;
    console.log(text_security);
}

//-- Obtiene el valor de la suma de los pesos de todos los elementos salvo el que se va a editar
function get_suma(com_list, element_to_edit) {
    suma = 0;
    for (let i = 0; i < com_list.length; i++) {
        suma += parseFloat(com_list[i].value);
    }
    element_value = parseFloat(document.getElementById(element_to_edit).value);
    suma -= element_value;
    return suma;
}

function set_max_attribute(element_to_edit, new_max) {
    document.getElementById(element_to_edit).setAttribute('max', new_max);
}