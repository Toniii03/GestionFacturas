    // esto lee los parametro de la funcion
    function getQueryParam(param) {
        let urlParams = new URLSearchParams(window.location.search);
        return urlParams.get(param);
    }

    function toggleVisibility2() {
        let ascendenteDiv = document.querySelector('.filtroOrdenadoAscendentefactura');
        let descendenteDiv = document.querySelector('.filtroOrdenadoDescendentefactura');
        console.log(ascendenteDiv);
        console.log(descendenteDiv);
        // lee la url que recibe
        let direccion = getQueryParam('direccion');
        const orden = getQueryParam('orden');

        ascendenteDiv.style.display = 'flex';
        descendenteDiv.style.display = 'none';

        if (direccion === 'asc') {
            ascendenteDiv.style.display = 'flex'; 
            descendenteDiv.style.display = 'none';  
        } else if (direccion === 'dsc') {
            ascendenteDiv.style.display = 'none';
            descendenteDiv.style.display = 'flex'; 
        }
    }  

    window.onload = function() {
        toggleVisibility2();
    };
