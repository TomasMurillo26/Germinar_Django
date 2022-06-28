def total_carro(request):
    total= 0
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total = total +int(value["precio"])
    else:
        total="Inicia sesión para seguir con la compra"
    return {"total_carro":total}