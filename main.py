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
    '''
    def actualizar_cliente(self):
        if self.codCliente in self.clientes:
            cliente = self.clientes[self.codCliente]
            print(cliente)
            self.clientes.update()
            print(cliente)
        else: 
            print("El cliente no existe")
    '''
    def borrar_cliente(self):
        if self.codCliente in self.clientes:
            del self.clientes[self.codCliente]
            print("Cliente borrado con exito")

    def visualizar_cliente(self):
        if not self.clientes:
            print("No hay clientes registrados")
        else:
            print("---Datos del cliente---")
            for self.codCliente, cliente in  self.clientes.items():
                print(self.clientes)


cliente1 = Clientes(1, "Ana", "Fernandez Garcia", "ToySL", "Gerente", 33213, "Asturias", 6827497482, "6/3/97")
cliente2 = Clientes(2, "Juan", "Gomez Perez", "HISL", "Empleado", 33208, "Asturias", 638754873, "15/7/85")
cliente1.registrar_cliente()
print("-------------------")
cliente2.registrar_cliente()
print("-------------------")
cliente1.borrar_cliente()
print("-------------------")
cliente1.visualizar_cliente()
print("-------------------")
cliente2.visualizar_cliente()


'''
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
'''
'''
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