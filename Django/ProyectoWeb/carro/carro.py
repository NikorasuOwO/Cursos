from carro import context_processor


class Carro:

    def __init__(self, request):
        self.request = request
        self.session = request.session

        carro = self.session.get("carro") # recuperamos el carro de la sesión

        if not carro:
            carro = self.session["carro"]={} # Instanciamos carro y la clave "carro" de la sesión

        #else: # Si el carro existe ya
        self.carro = carro # El atributo de clase carro = carro pre-existente



### Importante: aquí trabajamos solo con el carro atributoi de clase, no el carro de la sesión ###
    def agregar(self, producto):

        if(str(producto.id) not in self.carro.keys() ): # Si no encuentras el producto en el carro
            self.carro[producto.id] = { # El valor del diccionario carro con clave producto_id será el siguiente

                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio": float(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url

            }
            
        else:
            self.carro[str(producto.id)]["cantidad"] += 1
            self.carro[str(producto.id)]["precio"] += producto.precio
        
        self.guardar_carro()

    

    def guardar_carro(self):
        self.session["carro"] = self.carro # Ahora sí modificamos el carro de la sesión
        self.session.modified = True

    def eliminar(self, producto):
        
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    
    def restar_producto(self, producto):
        if(str(producto.id) in self.carro.keys()):

            self.carro[str(producto.id)]["cantidad"] -= 1
            self.carro[str(producto.id)]["precio"] -= producto.precio
            self.guardar_carro()

            if (self.carro[str(producto.id)]["cantidad"] < 1):
                self.eliminar(producto)


    def limpiar_carro(self):

        self.session["carro"]={} # Instanciamos carro y la clave "carro" de la sesión
        self.session.modified = True