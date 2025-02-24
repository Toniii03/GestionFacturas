    // esto lee los parametro de la funcion
    function getQueryParam(param) {
        let urlParams = new URLSearchParams(window.location.search);
        return urlParams.get(param);
    }

    function toggleVisibility() {
        let ascendenteDiv = document.querySelector('.filtroOrdenadoAscendente');
        let descendenteDiv = document.querySelector('.filtroOrdenadoDescendente');
        // lee la url que recibe
        const direccion = getQueryParam('direccion');
        const orden = getQueryParam('orden');
    
        if (orden === 'fecha_pago') {
            if (direccion === 'asc') {
                ascendenteDiv.style.display = 'flex';  
                descendenteDiv.style.display = 'none';  
            } else if (direccion === 'dsc') {
                ascendenteDiv.style.display = 'none';
                descendenteDiv.style.display = 'flex'; 
            }
        } else {
            ascendenteDiv.style.display = 'flex';
            descendenteDiv.style.display = 'none';
        }
    }

    function toggleVisibility2() {
        let ascendenteDiv = document.querySelector('.filtroOrdenadoAscendentefactura');
        let descendenteDiv = document.querySelector('.filtroOrdenadoDescendentefactura');
        console.log(ascendenteDiv);
        console.log(descendenteDiv);
        // lee la url que recibe
        let direccion = getQueryParam('direccion');
        const orden = getQueryParam('orden');
    
        if (orden === 'factura') {
            if (direccion === 'asc') {
                ascendenteDiv.style.display = 'flex'; 
                descendenteDiv.style.display = 'none';  
            } else if (direccion === 'dsc') {
                ascendenteDiv.style.display = 'none';
                descendenteDiv.style.display = 'flex'; 
            }
        } else {
            ascendenteDiv.style.display = 'flex';
            descendenteDiv.style.display = 'none';
        }
    }  
    //cuando carga la pagina se ejecuta estas 2 funciones
    window.onload = function() {
        toggleVisibility();
        toggleVisibility2();
    };