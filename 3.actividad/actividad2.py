class Producto:
    
    def __init__(self,nombre,precio,cantidad,categoría):
        self.__nombre=nombre
        self.__precio=precio
        self.cantidad=cantidad
        self.categoría=categoría
        
        #metodo getter
    def obtener_nombre(self):
        return self.__nombre
    
    def obtener_precio(self):
        return self.__precio
    
    
    #metodo setter
    def establecer_nombre(self, nuevo_nombre):
        self.__nombre=nuevo_nombre
        
    def establecer_precio(self, nuevo_precio):
        self.__precio=nuevo_precio
        
        
    
    #este metodo muestra detalles del objeto
    def mostrar_detalles(self):
        print(f"||||||||||||||||||||")
        print(f"\nNombres: {self.__nombre}")
        print(f"Precio: {self.__precio}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Categoría: {self.categoría}")
        
#objeto
productos=Producto("Colgate",3000,50,"Higiene")

#Imprimir atributos publicos y privados
productos.mostrar_detalles()

print("||||||||||||||||||||||")

#se imprimen los atributos encapsulados y modificados
productos.establecer_nombre("Listerine")
print(f"Nombres: { productos.obtener_nombre() }")
productos.establecer_precio("50000")
print(f"Precio: { productos.obtener_precio() }")
print(f"Cantidad: { productos.cantidad }")
print(f"Categoría: { productos.categoría }")
