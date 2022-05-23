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


    
    //***************************VALIDACIONES*************************************/
    $("#form-sus").validate({
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

    $("#form-usuario").validate({
        rules: {
            nombre: {
                required: true,
                minlength: 10
            },
            password: {
                required: true,
                minlength: 8
            },
            email: {
                required: true,
                email: true
            },
            direccion: {
                required: true,
                minlength: 10
            },
            fecha: {
                required: true,
                minlength: 2
            },
            comunaregion: {
                required: true,
            },
            terminos: {
                required: true,
            },
            reppassword: {
                equalTo: "#password",
                minlength: 8
            },
            tipopago: {
                required: true
            }
        },
        messages: {
            nombre: {
                required: "Debes ingresar tu nombre",
                minlength: "El campo debe tener mínimo 10 caracteres"
            },
            password: {
                required: "Debes crear una contraseña",
                minlength: "Tu contraseña debe tener mínimo 8 caracteres"
            },
            reppassword: {
                required: "Repite tu contraseña",
                equalTo: "Las contraseñas no coinciden",
                minlength: "Tu contraseña debe tener mínimo 8 caracteres"
            },
            email: {
                required: "Debes ingresar un correo electrónico",
                email: "El correo debe tener un @ incluido",
                minlength: "Tu correo debe tener mínimo 10 caracteres "
            },
            direccion: {
                required: "Debes ingresar tu dirección",
                minlength: "Tu direccion debe tener mínimo 10 caracteres"
            },
            fecha: {
                required: "Debes ingresar tu fecha de nacimiento"
            },
            terminos: {
                required: "Confirma los términos y condiciones"
            }
        }
    });
    //********************************EFECTOS****************************************/

    $('.tm-date').datepicker({
        format: "dd/mm/yyyy",
        clearBtn: true,
        language: "es",
        autoclose: true
    })
    //******************************CALENDARIO**************************************/

});