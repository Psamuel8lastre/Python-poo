#creo la clase
class FigurasGeometrica:
    #metodo constructor
    def __init__(self,nombre,color,lados,area,perimetro):
        #defino los atributos de instancia de la clase
        self.nombre = nombre 
        self.color = color
        self.lados = lados
        self.area = area
        self.perimetro = perimetro
        
    #mostramos informacion del objeto
    def muestra_detalles(self):
        print("---------------------------->")
        print("Informacion de la figura geometrica")
        print("---------------------------->")
        print(f"Nombre: {self.nombre}")
        print(f"Color: {self.color}")
        print(f"Lados: {self.lados}")
        print(f"Area: {self.area}")
        print(f"Perimetro: {self.perimetro}")
        
objeto1=FigurasGeometrica("Circulo","Rojo","0","78.54 cm","31.42 cm")
objeto2=FigurasGeometrica("Cuadrado","Azul","4","25 cm","20 cm")
objeto3=FigurasGeometrica("Triangulo","Verde","3","10.83 cm","18 cm")


objeto1.muestra_detalles()

#objeto2.muestra_detalles()
#objeto3.muestra_detalles()