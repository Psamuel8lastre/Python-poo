#creo la clase
class Motos:
    #metodo constructor
    def __init__(self,marca,modelo,cilindraje,color,combustible):
        #defino los atributos de instancia de la clase
        self.marca = marca 
        self.modelo = modelo
        self.cilindraje = cilindraje
        self.color = color
        self.combustible = combustible
        
    #mostramos informacion del objeto
    def muestra_detalles(self):
        print("---------------------------->")
        print("Informacion de la Moto")
        print("---------------------------->")
        print(f"marca: {self.marca}")
        print(f"modelo: {self.modelo}")
        print(f"Cilindraje: {self.cilindraje}")
        print(f"color: {self.color}")
        print(f"combustible: {self.combustible}")
        
    def encender(self):
        self.prender = input("Desea encender la moto: (y/n)")
        
        if self.prender == "y":
            print("La moto esta encendida correctamente")
            
        else:
            print(":(")
    def capacidad(self):
        self.personas = input("Ingrese el numero de pasajeros: ")
        
        if self.personas <= 3:
            print("Que tenga un buen viaje ;3")
            
        else:
            print("lo siento muchos pasajeros xd")
        
objeto1=Motos("Honda","Activa","110 cc","Rojo","Gasolina")
objeto2=Motos("Suzuki","Access","125 cc","Gris","Gasolina")
objeto3=Motos("Zero  Motocycle","SRLF","500 CC","nEGRA","Gasolina")


objeto1.muestra_detalles()

#objeto2.muestra_detalles()
#objeto3.muestra_detalles()