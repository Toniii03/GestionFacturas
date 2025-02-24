let articuloAñadidos = {};
let articulos = document.querySelector("#articulos").value;
articuloAñadidos = JSON.parse(articulos);

document.querySelector("#formularioo").addEventListener("submit", guardarFactura)

let inputDescuento = document.querySelector("#id_descuento");
inputDescuento.addEventListener("change", calcularTotalFactura);

let tabla = document.querySelector("table");
tabla.addEventListener("click", eliminarArticulo);

let inputIva = document.querySelector("#id_impuesto");
inputIva.addEventListener("change", calcularTotalFactura);

calcularTotalFactura()

function guardarFactura(event) {
  let articulos = JSON.stringify(articuloAñadidos);
  document.querySelector("#articulos_data").value = articulos;
  this.submit();
}

function actualizarListaArticulos() {

  let tabla = document.querySelector("table");
  let tbody = tabla.querySelector("tbody");
  tbody.innerHTML = "";
  for (let articulo of articuloAñadidos) {
    let fila = document.createElement("tr");

    let articuloId = document.createElement("td");
    articuloId.textContent = articulo.id;
    fila.appendChild(articuloId);
    tbody.appendChild(fila);

    let articuloNombre = document.createElement("td");
    articuloNombre.textContent = articulo.articulo;
    fila.appendChild(articuloNombre);

    let articuloCantidad = document.createElement("td");
    articuloCantidad.textContent = articulo.cantidad;
    fila.appendChild(articuloCantidad);

    let articuloPrecio = document.createElement("td");
    articuloPrecio.textContent = parseFloat(articulo.precio_unitario).toFixed(2);
    fila.appendChild(articuloPrecio);

    let tdImagenes = document.createElement("td");
    let divImagenes = document.createElement("div");
    divImagenes.classList.add("factura_articulo_eliminar");
    let imagen1 = document.createElement("img");
    imagen1.src = "../../static/images/papelera.png";
    imagen1.classList.add("imagenBasura1");
    divImagenes.appendChild(imagen1);

    let imagen2 = document.createElement("img");
    imagen2.src = "../../static/images/papelera (1).png";
    imagen2.classList.add("imagenBasura2");
    divImagenes.appendChild(imagen2);

    tdImagenes.appendChild(divImagenes);
    fila.appendChild(tdImagenes);
    tbody.appendChild(fila);
  }
}

function eliminarArticuloAñadido(idArticulo) {
  let nuevosArticuloAñadidos = [];
  if (articuloAñadidos.length > 1) {
    for (let articulo of articuloAñadidos) {
      if (articulo.id != idArticulo) {
        nuevosArticuloAñadidos.push(articulo);
      }
    }
    articuloAñadidos = nuevosArticuloAñadidos;
  } else {
    alert("No se puede eliminar el único articulo de la factura");
  }
}

function eliminarArticulo(event) {
  if (event.target.tagName === "IMG") {
    let divArticulo = event.target.parentNode.parentNode.parentNode;
    let idArticulo = divArticulo.querySelector("td:first-child").textContent;
    eliminarArticuloAñadido(idArticulo);
    actualizarListaArticulos();
    calcularTotalFactura();
  }
}

function calcularTotalFactura() {
  let totalPrecio = 0;
  let cantidad;
  let precio;

  for (let articulo of articuloAñadidos) {
    cantidad = articulo.cantidad;
    precio = articulo.precio_unitario;
    totalPrecio += precio * cantidad;
  }

  document.querySelector("#id_subtotal").value = totalPrecio;
  let iva = Number(document.querySelector("#id_impuesto").value) / 100;
  let impuesto = iva * totalPrecio;

  let descuento = Number(document.querySelector("#id_descuento").value) / 100;
  let descontar = totalPrecio * descuento;

  document.querySelector("#id_total").value = totalPrecio + impuesto - descontar;

}
