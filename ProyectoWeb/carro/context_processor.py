from suscripcion.views import  get_user_membership

def total_carro(request):
    total= 0
    
    if request.user.is_authenticated:
        
        for key, value in request.session["carro"].items():
            membresia_actual = get_user_membership(request)
            mem = membresia_actual.tipoMembresia
            print(mem)
            if str(mem) == 'Germinar':
                total = total +int(value["precio"])
                descuento = 0.05*total 
                total_final = int(total - descuento)
            else:
                total = total +int(value["precio"])
                total_final = total
    else:
        total_final="Inicia sesión para seguir con la compra"
    return {"total_carro":total_final}