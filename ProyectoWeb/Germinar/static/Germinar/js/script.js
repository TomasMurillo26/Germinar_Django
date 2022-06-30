$(document).ready(function () {
    //console.log('funcionando');
    //$('.error-correo').html('Está funcionando?');

    //$('#val-correo').remove(); remover el h3
    //$('#val-correo').hide(); //esconder el h3
    //$(selector).attr(attributeName, value); //para añadir imagenes al html desde jquery 


    //$('.btn-sus').click(function () { 
    //    $('#val-correo').addClass('val-correo');
    //    $('#val-correo').append('<h3 id="error-correo">Hola</h3>');//annadir codigo html a través de jquery
    //});

    //$('.btn-sus').click(function () { 
    //  $('#val-correo').removeClass('val-correo'); 
    //});
    $('#cuadro-donaciones').hide(0);
    $(window).scroll(function () {
        var windowHeight = $(window).scrollTop();
        var historia = $('#historia').offset();
        historia = historia.top;

        if (windowHeight >= historia) {
            $('#cuadro-donaciones').fadeIn(1500);

        } else {
            $('#cuadro-donaciones').fadeOut(100);
        }
    });


    const $seleccionArchivos = document.querySelector("#seleccionArchivos"),
        $imagenPrevisualizacion = document.querySelector("#imagenPrevisualizacion");

    // Escuchar cuando cambie
    $seleccionArchivos.addEventListener("change", () => {
        // Los archivos seleccionados, pueden ser muchos o uno
        const archivos = $seleccionArchivos.files;
        // Si no hay archivos salimos de la función y quitamos la imagen
        if (!archivos || !archivos.length) {
            $imagenPrevisualizacion.src = "";
            return;
        }
        // Ahora tomamos el primer archivo, el cual vamos a previsualizar
        const primerArchivo = archivos[0];
        // Lo convertimos a un objeto de tipo objectURL
        const objectURL = URL.createObjectURL(primerArchivo);
        // Y a la fuente de la imagen le ponemos el objectURL
        $imagenPrevisualizacion.src = objectURL;
    });

    //***************************VALIDACIONES*************************************/
    $.tools.validator.localize("fi", {
        '*'          : 'Virheellinen arvo',
        ':email'     : 'Virheellinen s&auml;hk&ouml;postiosoite',
        ':number'    : 'Arvon on oltava numeerinen',
        ':url'       : 'Virheellinen URL',
        '[max]'      : 'Arvon on oltava pienempi, kuin $1',
        '[min]'      : 'Arvon on oltava suurempi, kuin $1',
        '[required]' : 'Kent&auml;n arvo on annettava'
    });

    $("#form-sus").validate({
        lang: 'fi',
        rules: {
            email: {
                email: true
            }
        },
        messages: {
            email: {
                email: "El correo debe tener un @ incluido",
                minlength: "Tu correo debe tener mínimo 10 caracteres "
            }
        }
    });


    $("#form-producto").validate({
        language: 'fi',
        rules: {
            nombreProd: {
                required: true,
                minlength: 5
            },
            cantidad: {
                required: true,
                min: 1,
                number: true
            },
            precio: {
                required: true,
                number: true
            },
            categoria: {
                required: true,
            },
            descripcion: {
                minlength: 100
            },
            seleccionaArchivos: {
                required: true,
                url: true
            },
        },
        messages: {
            nombreProd: {
                required: "Debes ingresar el nombre del producto",
                minlength: "El campo debe tener mínimo 10 caracteres"
            },
            cantidad: {
                required: "Debes ingresar una cantidad",
                min:"Mínimo 1 producto"
            },
            precio: {
                required: "Debes ingresar el precio del producto",
                number: "Debes ingresar solo números"
            },
            categoria: {
                required: "Debes seleccionar una categoría"
            },
            direccion: {
                minlength: "La descripción minímo debe tener 100 caracteres"
            },
            seleccionArchivos: {
                required: "Debes subir una imagen de tu producto",
                url: "Ingresa una imagen con una url valida"
            },
        }
    });   
    //********************************EFECTOS****************************************/



    $(document).ready(function habilitarbtn() {
        {
            var nombre = $('#nombre').val();
            var password = $('#password').val();
            var email = $('#email').val();
            var direccion = $('#direccion').val();
            var reppassword = $('#reppassword').val();
            var comunaregion = $('.tam-region').val();
            var fecha = $('#fecha').val();

            if (nombre && password && email && direccion && reppassword && comunaregion && fecha && terminos ) {
                $('#submitButton').attr('disabled', false);
                $('#submitButton').removeClass('lost');
                $('#submitButton').addClass('found');
            } else {
                $('#submitButton').attr('disabled', true);
                $('#submitButton').removeClass('found');
                $('#submitButton').addClass('lost');
            }
        }
    })

    $(document).ready(function mostrarContrasena() {
            var tipo = document.getElementById("password");
            if (tipo.type == "password") {
                tipo.type = "text";
            } else {
                tipo.type = "password";
            }
        })
    /* Fichero /js/validate.es.js */
    //******************************CALENDARIO**************************************/


    





});