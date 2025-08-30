class Clientes:
    def __init__(self, codCliente, nombre, apellidos, empresa, puesto, cp, provincia, telefono, fechaNacimiento):
        self.codCliente = codCliente
        self.nombre = nombre
        self.apellidos = apellidos
        self.empresa = empresa
        self.puesto = puesto
        self.cp = cp
        self.provincia = provincia
        self.telefono = telefono
        self.fechaNacimiento = fechaNacimiento

        self.clientes = {}

    def registrar_cliente(self):

        nuevoCliente = {
            "codCliente": self.codCliente,
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "empresa": self.empresa,
            "puesto": self.puesto,
            "cp": self.cp,
            "provincia": self.provincia,
            "telefono": self.telefono,
            "fechaNacimiento": self.fechaNacimiento
        }
        #Registramos al cliente dentro del diccionario principal
        self.clientes[self.codCliente] = nuevoCliente

        print("Cliente registrado correctamente")
        print(f"{self.clientes}")

    def actualizar_cliente(self):
        if self.codCliente in self.clientes:
            cliente = self.clientes[self.codCliente]
            print(cliente)


cliente1 = Clientes(1, "Ana", "Fernandez Garcia", "ToySL", "Gerente", 33213, "Asturias", 6827497482, 6/3/97)
cliente1.registrar_cliente()
'''
    def actualizar_cliente():
        pass
    def borrar_cliente():
        pass
    def visualizar_cliente():
        pass

class Articulos:
    def __init__(self, codArticulo, nombre, descripcion, precioUnidad, unidadesStock, stockSeguridad, imagen):
        self.codArticulo = codArticulo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precioUnidad = precioUnidad
        self.unidadesStock = unidadesStock
        self.stockSeguridad = stockSeguridad
        self.imagen = imagen

        articulos = {}
    
    def registrar_articulo():
        pass
    def actualizar_articulo():
        pass
    def borrar_articulo():
        pass
    def visualizar_articulo():
        pass

class Compra(Clientes, Articulos):
    def __init__(self, codCliente, codArticulo, fecha, unidades):
        Clientes().__init__(codCliente)
        Articulos().__init__(codArticulo)
        self.fecha = fecha
        self.unidades = unidades

        compras = {}

    def registrar_compra():
        pass
    def actualizar_compra():
        pass
    def borrar_compra():
        pass
    def visualizar_compra():
        pass
'''