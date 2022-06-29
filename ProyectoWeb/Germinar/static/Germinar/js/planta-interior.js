$(document).ready(function(){
        fetch('https://joxcastro.github.io/listaPlantasApi/categoria/planta-interior.json')
            .then(res => {
                if (res.ok == true){
                    console.log("Get successful")
                } else {
                    console.log("Get error")
                }
                return res
            })
            .then(res => res.json())
            .then(data => {
                $.each(data,function(i,item){
                    function format(num) {
                        var array = num.toString().split('');
                        var index = -3;
                        while (array.length + index > 0){
                            array.splice(index, 0 , ',');
                            index -= 4;
                        }
                        return array.join('');
                    };
                    precio = format(item.precio)
                    $("#productoCiclo").append(`<div class="producto" type="submit" id="enviar" value="Ver producto"><form action="{% url 'formulario' %}" id="formPlanta"><div class="producto__imagen"><input type="text" name="categoria" id="categoria" value="${item.categoria}" style="display: none;"> <input type="text" name="id" id="id" value="${item.id}" style="display: none;"><img src="${item.img}" alt="imagen planta"></div><div class="producto__informacion"><p class="producto__nombre">${item.nomPlant}</p><p class="producto__precio">\$${precio}</p><input type="submit" class="btn btn-primary" id="enviar" value="Ver producto"></div></form></div>`);
                    if(item.id == id){
                        $("#productoPlanta").append('<div class="contenedor2"><main class="plantas_cuadro contenedor3"><div class="planta_img"><img src="'+item.img+'" ></div><div class="planta_info"><h1>'+item.nomPlant+'</h1><h2>$'+precio+'</h2><div class="info_cliente"><h3>Producto en venta por: <span>'+item.vendedor+'</span></h3><h3>Stock: '+item.cantidad+'</h3></div><p>'+item.desc+'</p><form action="#" method="get" class="formulario-compra" name="form-compra" id="form-compra"><div class="boton"><input type="number" name="cantidad" id="cantidad" placeholder="Cantidad" min="1" max="'+item.cantidad+'"><div><button type="submit" class="btn btn-secondary btn-sm ">Agregar al carrito</button><button type="submit" class="btn btn-secondary btn-sm ">comprar</button></div></div></form></div></main></div><div class="boton-volver contenedor2"></div>');
                    }
                })
                console.log(data)
            })
    });

