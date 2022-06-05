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

    $("#form-usuario").validate({
        lang: 'fi',
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

    $('.tm-date').datepicker({
        format: "dd/mm/yyyy",
        clearBtn: true,
        language: "es",
        autoclose: true
    })

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


    $(document).ready(function myFunction() {
        var input, filtro, tabla, tr, td, i, txtValue;
        input = document.getElementById("nombreProd");
        filtro = input.value.toUpperCase();
        tabla = document.getElementById("tabla-prod");
        tr = tabla.getElementsByTagName("tr");
        for (i = 0; i < tr.length; i++) {
            td = tr[i].getElementsByTagName("td")[0];
            if (td) {
                txtValue = td.textContent || td.innerText;
                if (txtValue.toUpperCase().indexOf(filtro) > -1) {
                    tr[i].style.display = "";
                } else {
                    tr[i].style.display = "none";
                }
            }       
        }
    })
    /* Fichero /js/validate.es.js */
    //******************************CALENDARIO**************************************/
    var RegionesYcomunas = {

        "regiones": [{
            "NombreRegion": "Arica y Parinacota",
            "comunas": ["Arica", "Camarones", "Putre", "General Lagos"]
        },
        {
            "NombreRegion": "Tarapacá",
            "comunas": ["Iquique", "Alto Hospicio", "Pozo Almonte", "Camiña", "Colchane", "Huara", "Pica"]
        },
        {
            "NombreRegion": "Antofagasta",
            "comunas": ["Antofagasta", "Mejillones", "Sierra Gorda", "Taltal", "Calama", "Ollagüe", "San Pedro de Atacama", "Tocopilla", "María Elena"]
        },
        {
            "NombreRegion": "Atacama",
            "comunas": ["Copiapó", "Caldera", "Tierra Amarilla", "Chañaral", "Diego de Almagro", "Vallenar", "Alto del Carmen", "Freirina", "Huasco"]
        },
        {
            "NombreRegion": "Coquimbo",
            "comunas": ["La Serena", "Coquimbo", "Andacollo", "La Higuera", "Paiguano", "Vicuña", "Illapel", "Canela", "Los Vilos", "Salamanca", "Ovalle", "Combarbalá", "Monte Patria", "Punitaqui", "Río Hurtado"]
        },
        {
            "NombreRegion": "Valparaíso",
            "comunas": ["Valparaíso", "Casablanca", "Concón", "Juan Fernández", "Puchuncaví", "Quintero", "Viña del Mar", "Isla de Pascua", "Los Andes", "Calle Larga", "Rinconada", "San Esteban", "La Ligua", "Cabildo", "Papudo", "Petorca", "Zapallar", "Quillota", "Calera", "Hijuelas", "La Cruz", "Nogales", "San Antonio", "Algarrobo", "Cartagena", "El Quisco", "El Tabo", "Santo Domingo", "San Felipe", "Catemu", "Llaillay", "Panquehue", "Putaendo", "Santa María", "Quilpué", "Limache", "Olmué", "Villa Alemana"]
        },
        {
            "NombreRegion": "Región del Libertador Gral. Bernardo O’Higgins",
            "comunas": ["Rancagua", "Codegua", "Coinco", "Coltauco", "Doñihue", "Graneros", "Las Cabras", "Machalí", "Malloa", "Mostazal", "Olivar", "Peumo", "Pichidegua", "Quinta de Tilcoco", "Rengo", "Requínoa", "San Vicente", "Pichilemu", "La Estrella", "Litueche", "Marchihue", "Navidad", "Paredones", "San Fernando", "Chépica", "Chimbarongo", "Lolol", "Nancagua", "Palmilla", "Peralillo", "Placilla", "Pumanque", "Santa Cruz"]
        },
        {
            "NombreRegion": "Región del Maule",
            "comunas": ["Talca", "ConsVtución", "Curepto", "Empedrado", "Maule", "Pelarco", "Pencahue", "Río Claro", "San Clemente", "San Rafael", "Cauquenes", "Chanco", "Pelluhue", "Curicó", "Hualañé", "Licantén", "Molina", "Rauco", "Romeral", "Sagrada Familia", "Teno", "Vichuquén", "Linares", "Colbún", "Longaví", "Parral", "ReVro", "San Javier", "Villa Alegre", "Yerbas Buenas"]
        },
        {
            "NombreRegion": "Región del Biobío",
            "comunas": ["Concepción", "Coronel", "Chiguayante", "Florida", "Hualqui", "Lota", "Penco", "San Pedro de la Paz", "Santa Juana", "Talcahuano", "Tomé", "Hualpén", "Lebu", "Arauco", "Cañete", "Contulmo", "Curanilahue", "Los Álamos", "Tirúa", "Los Ángeles", "Antuco", "Cabrero", "Laja", "Mulchén", "Nacimiento", "Negrete", "Quilaco", "Quilleco", "San Rosendo", "Santa Bárbara", "Tucapel", "Yumbel", "Alto Biobío", "Chillán", "Bulnes", "Cobquecura", "Coelemu", "Coihueco", "Chillán Viejo", "El Carmen", "Ninhue", "Ñiquén", "Pemuco", "Pinto", "Portezuelo", "Quillón", "Quirihue", "Ránquil", "San Carlos", "San Fabián", "San Ignacio", "San Nicolás", "Treguaco", "Yungay"]
        },
        {
            "NombreRegion": "Región de la Araucanía",
            "comunas": ["Temuco", "Carahue", "Cunco", "Curarrehue", "Freire", "Galvarino", "Gorbea", "Lautaro", "Loncoche", "Melipeuco", "Nueva Imperial", "Padre las Casas", "Perquenco", "Pitrufquén", "Pucón", "Saavedra", "Teodoro Schmidt", "Toltén", "Vilcún", "Villarrica", "Cholchol", "Angol", "Collipulli", "Curacautín", "Ercilla", "Lonquimay", "Los Sauces", "Lumaco", "Purén", "Renaico", "Traiguén", "Victoria",]
        },
        {
            "NombreRegion": "Región de Los Ríos",
            "comunas": ["Valdivia", "Corral", "Lanco", "Los Lagos", "Máfil", "Mariquina", "Paillaco", "Panguipulli", "La Unión", "Futrono", "Lago Ranco", "Río Bueno"]
        },
        {
            "NombreRegion": "Región de Los Lagos",
            "comunas": ["Puerto Montt", "Calbuco", "Cochamó", "Fresia", "FruVllar", "Los Muermos", "Llanquihue", "Maullín", "Puerto Varas", "Castro", "Ancud", "Chonchi", "Curaco de Vélez", "Dalcahue", "Puqueldón", "Queilén", "Quellón", "Quemchi", "Quinchao", "Osorno", "Puerto Octay", "Purranque", "Puyehue", "Río Negro", "San Juan de la Costa", "San Pablo", "Chaitén", "Futaleufú", "Hualaihué", "Palena"]
        },
        {
            "NombreRegion": "Región Aisén del Gral. Carlos Ibáñez del Campo",
            "comunas": ["Coihaique", "Lago Verde", "Aisén", "Cisnes", "Guaitecas", "Cochrane", "O’Higgins", "Tortel", "Chile Chico", "Río Ibáñez"]
        },
        {
            "NombreRegion": "Región de Magallanes y de la AntárVca Chilena",
            "comunas": ["Punta Arenas", "Laguna Blanca", "Río Verde", "San Gregorio", "Cabo de Hornos (Ex Navarino)", "AntárVca", "Porvenir", "Primavera", "Timaukel", "Natales", "Torres del Paine"]
        },
        {
            "NombreRegion": "Región Metropolitana de Santiago",
            "comunas": ["Cerrillos", "Cerro Navia", "Conchalí", "El Bosque", "Estación Central", "Huechuraba", "Independencia", "La Cisterna", "La Florida", "La Granja", "La Pintana", "La Reina", "Las Condes", "Lo Barnechea", "Lo Espejo", "Lo Prado", "Macul", "Maipú", "Ñuñoa", "Pedro Aguirre Cerda", "Peñalolén", "Providencia", "Pudahuel", "Quilicura", "Quinta Normal", "Recoleta", "Renca", "San Joaquín", "San Miguel", "San Ramón", "Vitacura", "Puente Alto", "Pirque", "San José de Maipo", "Colina", "Lampa", "TilVl", "San Bernardo", "Buin", "Calera de Tango", "Paine", "Melipilla", "Alhué", "Curacaví", "María Pinto", "San Pedro", "Talagante", "El Monte", "Isla de Maipo", "Padre Hurtado", "Peñaflor"]
        }]
    }


    jQuery(document).ready(function () {

        var iRegion = 0;
        var htmlRegion = '<option value="sin-region">Seleccione región</option><option value="sin-region">---</option>';
        var htmlComunas = '<option value="sin-region">Seleccione comuna</option><option value="sin-region">---</option>';

        jQuery.each(RegionesYcomunas.regiones, function () {
            htmlRegion = htmlRegion + '<option value="' + RegionesYcomunas.regiones[iRegion].NombreRegion + '">' + RegionesYcomunas.regiones[iRegion].NombreRegion + '</option>';
            iRegion++;
        });

        jQuery('#regiones').html(htmlRegion);
        jQuery('#comunas').html(htmlComunas);

        jQuery('#regiones').change(function () {
            var iRegiones = 0;
            var valorRegion = jQuery(this).val();
            var htmlComuna = '<option value="sin-comuna">Seleccione comuna</option><option value="sin-comuna">---</option>';
            jQuery.each(RegionesYcomunas.regiones, function () {
                if (RegionesYcomunas.regiones[iRegiones].NombreRegion == valorRegion) {
                    var iComunas = 0;
                    jQuery.each(RegionesYcomunas.regiones[iRegiones].comunas, function () {
                        htmlComuna = htmlComuna + '<option value="' + RegionesYcomunas.regiones[iRegiones].comunas[iComunas] + '">' + RegionesYcomunas.regiones[iRegiones].comunas[iComunas] + '</option>';
                        iComunas++;
                    });
                }
                iRegiones++;
            });
            jQuery('#comunas').html(htmlComuna);
        });
        jQuery('#comunas').change(function () {
            if (jQuery(this).val() == 'sin-region') {
                alert('Seleccione alguna region');
            } else if (jQuery(this).val() == 'sin-comuna') {
                alert('Seleccione alguna comuna');
            }
        });
        jQuery('#regiones').change(function () {
            if (jQuery(this).val() == 'sin-region') {
                alert('Seleccione alguna region');
            }
        });

    });


});