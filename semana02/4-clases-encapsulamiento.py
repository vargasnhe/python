#encapsulamiento de clases es el metodo de ocuilatar los atributos de una clase para que no puedan ser modificados por el usuario 
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
        self.__ventas = []
        self._preciomayorista = 100
    
    def generar_venta(self, fecha, cliente, cantidad): 
        venta = {
            "fecha": fecha,
            "cliente": cliente,
            "cantidad": cantidad
        }
        self.__ventas.append(venta)
        print("venta generada")
        
    def mostrar_ventas(self):
        print(self.__ventas)
        
detergente = Producto("sapito", 4.5, 50)
detergente.nombre = "lechuga"
print(detergente.nombre)

detergente.generar_venta(fecha='2022-10-19', cliente='Eduardo de Rivero', cantidad=10)
detergente.generar_venta(fecha='2022-10-29', cliente='Julissa Perez', cantidad=30)
detergente.generar_venta(fecha='2022-10-30', cliente='Franco Portugal', cantidad=20)
detergente.generar_venta(fecha='2022-11-02', cliente='Michelle Ordoñez', cantidad=15)

print(detergente.mostrar_ventas())
