from requests import session

class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"]={}
        self.carro = carro

    def agregar(self,producto):
        if(str(producto.idProducto) not in self.carro.keys()):
            self.carro[producto.idProducto]={
                "idProducto": producto.idProducto,
                "nombreProducto": producto.nombreProducto,
                "precio": str(producto.precio),
                "cantidad":1,
                "imagenProducto": producto.imagenProducto.url
            }
        else:
            for key, value in self.carro.items():
                if key==str(producto.idProducto):
                    value["cantidad"]=value["cantidad"]+1
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self,producto):
        producto.idProducto = str(producto.idProducto)
        if producto.idProducto in self.carro:
            del self.carro[producto.idProducto]
            self.guardar_carro()
        
    def restar_producto(self,producto):
        for key, value in self.carro.items():
            if key==str(producto.idProducto):
                value["cantidad"]=value["cantidad"]-1
                if value["cantidad"]<1:
                    self.eliminar(producto)
                break
            else:
                print("El producto no existe en el carrito")
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified = True
