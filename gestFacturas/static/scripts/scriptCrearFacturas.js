let articuloAñadidos = {};

let btnAñadirARticulo = document.querySelector(".boton_aniadir_articulo");
btnAñadirARticulo.addEventListener("click", añadirArticulo);

let inputDescuento = document.querySelector("#id_descuento")
inputDescuento.addEventListener("change", calcularTotalFactura)

let inputIva = document.querySelector("#id_impuesto")
inputIva.addEventListener("change", calcularTotalFactura)


function abrir_modal_Empresas(url) {
    let $ = jQuery.noConflict();
    $('#modalCrearEmpresa').load(url, function () {
        $(this).modal('show');
    });
}


function abrir_modal_cliente(url) {
    console.log("cargar modal")
    let $ = jQuery.noConflict();
    $('#modalCrearCliente').load(url, function () {
        $(this).modal('show');
    });
}

document.getElementById("formularioo").addEventListener("submit", function (event) {
    event.preventDefault();
    let cont = 0
    for (let articulo in articuloAñadidos) {
        cont++;
    }

    if (cont == 0) {
        //cambiar por mensajeError
        alert("No hay artículos añadidos a la factura.");
    } else {
        document.getElementById('articulos_data').value = JSON.stringify(articuloAñadidos);
        this.submit();
    }
})

function calcularTotalFactura() {
    let totalPrecio = 0;
    let cantidad;
    let precio;

    for (let articulo in articuloAñadidos) {
        cantidad = articuloAñadidos[articulo][0];
        precio = articuloAñadidos[articulo][1];
        totalPrecio += precio * cantidad;
    }

    document.querySelector("#id_subtotal").value = totalPrecio.toFixed(2);
    let iva = Number(document.querySelector('#id_impuesto').value) / 100;
    let impuesto = iva * totalPrecio;

    let descuento = Number(document.querySelector("#id_descuento").value) / 100;
    let descontar = totalPrecio * descuento;

    document.querySelector('#id_total').value = ((totalPrecio + impuesto) - descontar).toFixed(2);

}

function mostrarAlerta(mensaje) {

    let divMostrarMensaje = document.querySelector(".articulos_alertas");
    divMostrarMensaje.style.display = "block";
    divMostrarMensaje.style.opacity = "0";
    divMostrarMensaje.style.backgroundColor = "transparent"
    divMostrarMensaje.style.color = "red";

    let mensajeAlerta = document.createElement("p")
    mensajeAlerta.innerHTML = mensaje;
    mensajeAlerta.style.color = "red"

    divMostrarMensaje.appendChild(mensajeAlerta);

    setTimeout(function () {
        divMostrarMensaje.style.opacity = "1";
        divMostrarMensaje.style.color = "red";
    }, 200);

}

function mostrarMensaje(mensaje) {

    let divMostrarMensaje = document.querySelector(".articulos_alertas");
    divMostrarMensaje.style.display = "flex";
    divMostrarMensaje.style.alignItems = "center"
    divMostrarMensaje.style.transition = "opacity 1s";

    setTimeout(function () {
        divMostrarMensaje.style.opacity = "0";
    }, 2000);

    let mensajeAlerta = document.createElement("p");
    mensajeAlerta.innerHTML = mensaje;
    mensajeAlerta.style.color = "green"

    divMostrarMensaje.appendChild(mensajeAlerta);

    setTimeout(function () {
        divMostrarMensaje.style.opacity = "1";
        divMostrarMensaje.style.color = "red";
    }, 200);
}

function actualizarLista(resetear = false) {
    let totalPrecio = 0;

    let divmostrarArticulos = document.querySelector(".articuloAñadidos");

    if (resetear) {
        divmostrarArticulos.innerHTML = "";
    }

    let divarticuloIndividual = document.createElement("div");
    divarticuloIndividual.classList.add('articulosIndividuales');
    divmostrarArticulos.appendChild(divarticuloIndividual);

    let oArticulo;
    let cantidad;
    let precio;

    for (let articulo in articuloAñadidos) {
        oArticulo = articulo;
        cantidad = articuloAñadidos[articulo][0];
        precio = articuloAñadidos[articulo][1];
    }

    let pNombre = document.createElement("p");
    pNombre.classList.add('articuloInd');
    pNombre.innerHTML = "Artículo: " + oArticulo;

    let pCantidad = document.createElement("p");
    pCantidad.classList.add('articuloInd');
    pCantidad.innerHTML = "Cantidad: " + cantidad;

    let pPrecio = document.createElement("p");
    pPrecio.classList.add('articuloInd');
    pPrecio.innerHTML = "Precio: " + precio + "€";

    divarticuloIndividual.appendChild(pNombre);
    divarticuloIndividual.appendChild(pCantidad);
    divarticuloIndividual.appendChild(pPrecio);

    calcularTotalFactura();
}


function añadirArticulo() {
    document.querySelector(".articulos_alertas").innerHTML = "";
    let nombreArticulo = document.querySelector("#factArticulo").value;
    let cantidadArticulo = parseInt(document.querySelector("#id_cantidad").value, 10);
    let precioUnitarioArticulo = parseFloat(document.querySelector("#id_precio_unitario").value);

    if (nombreArticulo !== "") {
        if (cantidadArticulo > 0) {
            if (precioUnitarioArticulo > 0) {
                articuloAñadidos[nombreArticulo] = [cantidadArticulo, precioUnitarioArticulo];
                mostrarMensaje("Artículo añadido correctamente");
                actualizarLista();
                document.querySelector("#factArticulo").value = "";
                document.querySelector("#id_cantidad").value = "";
                document.querySelector("#id_precio_unitario").value = "";
            } else {
                mostrarAlerta("El precio tiene que ser mayor que 0");
            }
        } else {
            mostrarAlerta("La cantidad tiene que ser mayor que 0");
        }
    } else {
        mostrarAlerta("Necesitas el nombre de un artículo");
    }
}

