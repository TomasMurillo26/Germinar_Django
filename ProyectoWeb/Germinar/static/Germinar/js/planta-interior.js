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
                    $("#productoCiclo").append('<div class="producto"><a href="planta1.html"><div class="producto__imagen"><img src="'+item.img+'" alt="imagen planta"></div><div class="producto__informacion"><p class="producto__nombre">'+item.nomPlant+'</p><p class="producto__precio">$'+precio+'</p></div></a></div>');
                })
                console.log(data)
            })
    });

