
/*---
Función para procesar los parámetros recibidos en el URL
*/
function getQueryParams(qs) {
    qs = qs.split('+').join(' ');

    var params = {},
        tokens,
        re = /[?&]?([^=]+)=([^&]*)/g;

    while (tokens = re.exec(qs)) {
        params[decodeURIComponent(tokens[1])] = decodeURIComponent(tokens[2]);
    }

    return params;
}

/*---
Extrae del URL el id de cliente ya validado, su nombre, contacto y la última fecha de login, actualiza banner de seguridad
*/
console.log("ver la locacion"+document.location.search)
var query = getQueryParams(document.location.search);
console.log("id received is("+query.id+")");
console.log("id received is("+query.nombre+")");
console.log("id received is("+query.contacto+")");
console.log("id received is("+query.ultimo+")");
document.getElementById("lastlogin").innerHTML = "<table><tr><td>Cliente</td><td>"+query.id+"</td></tr><tr><td>Nombre</td><td>"+query.nombre+"</td></tr><tr><td>Contacto</td><td>"+query.contacto+"</td></tr><tr><td>Ultimo ingreso</td><td>"+query.ultimo+"</td></tr></table>";


/*---
Accede a REST API para obtener tickets
Tener en cuenta que typicode es un fake REST API
*/

// const APIREST_URL='http://my-json-server.typicode.com/lu7did/testJASON/ticket/';
const APIREST_URL='https://wabed4lrb4.execute-api.us-east-2.amazonaws.com/listarTicketGET?clienteID='+query.id;


//clientID 0533a95d-7eef-4c6b-b753-1a41c9d1fbd0

const api_TicketURL=APIREST_URL;
const HTMLResponse=document.querySelector("#app");

fetch(`${api_TicketURL}`)
.then(res => {
    return res.json();
}).then(ticket=>{
    console.log(ticket);
    let f=false;
    let table=document.createElement("table");
    table.style.border="1px solid";
    table.style.backgroundColor="#ADD8E6";
    ticket.forEach((t)=> {
        if (t.clienteID == query.id) {
            if (f==false) {

                f=true;
                const hdr=["Cliente","ID","Motivo","Estado","Fecha"];
                let tr=document.createElement("tr");
                tr.style.border="1px solid";
                hdr.forEach((item) => {
                    let th=document.createElement("th");
                    th.style.border="1px solid";

                    th.innerText = item;
                    tr.appendChild(th);
                });
                table.appendChild(tr);                   
            }

            const body=[t.clienteID,`${t.id}`,`${t.solucion}`,`${t.estado_solucion}`,`${t.ultimo_contacto}`];
            let trl=document.createElement("tr");
            body.forEach((line) => {
                let td=document.createElement("td");
                td.style.border="1px solid";
                td.innerText = line;
                trl.appendChild(td);
            });
            table.appendChild(trl);                   

        }
    });

    if (f) {
        HTMLResponse.appendChild(table);
    } else {

        console.log("no tiene tickets");
        document.getElementById('mensajes').style.textAlign = "center";
        document.getElementById('mensajes').style.color="RED";
        document.getElementById("mensajes").innerHTML = "No hay tickets pendientes";
    }
});

//          if (users.response == 'OK') {         //<==Habilitar esto para dejar que el API REST verifique sin exponer la password



/*---
Accede al REST API de tickets para obtener información
*/

/*
fetch(`${api_TicketURL}`)
.then((response)=>response.json())
.then((ticket)=>{
    let f=false;
    let table=document.createElement("table");
    ticket.forEach((t)=> {
        if (t.clienteID == query.id) {
            if (f==false) {

                f=true;
                const hdr=["Cliente","ID","Motivo","Estado","Fecha"];
                let tr=document.createElement("tr");
                hdr.forEach((item) => {
                    let th=document.createElement("th");
                    th.innerText = item;
                    tr.appendChild(th);
                });
                table.appendChild(tr);                   
            }

            const body=[t.clienteID,`${t.id}`,`${t.solucion}`,`${t.estado_solucion}`,`${t.ultimo_contacto}`];
            let trl=document.createElement("tr");
            body.forEach((line) => {
                let td=document.createElement("td");
                td.innerText = line;
                trl.appendChild(td);
            });
            table.appendChild(trl);                   

        }
    });

    if (f) {
        HTMLResponse.appendChild(table);
    } else {

        console.log("no tiene tickets");
        document.getElementById('mensajes').style.textAlign = "center";
        document.getElementById('mensajes').style.color="RED";
        document.getElementById("mensajes").innerHTML = "No hay tickets pendientes";
    }
});
*/    



