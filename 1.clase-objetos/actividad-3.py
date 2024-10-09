#creo la clase
class Carros:
    #metodo constructor
    def __init__(self,marca,modelo,año,color,combustible):
        #defino los atributos de instancia de la clase
        self.marca = marca 
        self.modelo = modelo
        self.año = año
        self.color = color
        self.combustible = combustible
        
    #mostramos informacion del objeto
    def muestra_detalles(self):
        print("---------------------------->")
        print("Informacion del Carro")
        print("---------------------------->")
        print(f"marca: {self.marca}")
        print(f"modelo: {self.modelo}")
        print(f"año: {self.año}")
        print(f"color: {self.color}")
        print(f"combustible: {self.combustible}")
        
    def encender(self):
        self.prender = input("Desea encender el carro: (y/n)")
        
        if self.prender == "y":
            print("El auto esta encendido correctamente")
            
        else:
            print(":(")
    def capacidad(self):
        self.personas = input("Ingrese el numero de pasajeros: ")
        
        if self.personas <= 4:
            print("Que tenga un buen viaje ;3")
            
        else:
            print("lo siento muchos pasajeros xd")
        
objeto1=Carros("Toyota","Corolla","2020","Rojo","Gasolina")
objeto2=Carros("Ford","Mustang","2018","Negro","Gasolina")
objeto3=Carros("Tesla","Modelo 3","022","Blanco","Electrico")


objeto1.muestra_detalles()
objeto1.encender()
objeto1.capacidad()
#objeto2.muestra_detalles()
#objeto3.muestra_detalles()