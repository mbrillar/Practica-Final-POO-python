class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = float(precio)
        self.cantidad = cantidad
    
    def actualizar_cantidad(self, cantidad):
        self.cantidad = cantidad

    def mostrar_informacion(self):
        return f"Producto: {self.nombre}, Categoria: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"