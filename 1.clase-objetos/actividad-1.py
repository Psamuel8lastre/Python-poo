#creo la clase
class Celular:
    #metodo constructor
    def __init__(self,nombre,marca,almacenamiento,ram,bateria):
        #defino los atributos de instancia de la clase
        self.nombre = nombre 
        self.marca = marca
        self.almacenamiento = almacenamiento
        self.ram = ram
        self.bateria = bateria
        
#mostramos informacion del objeto
    def muestra_detalles(self):
        print("---------------------------->")
        print("Informacion del celular")
        print("---------------------------->")
        print(f"Nombre: {self.nombre}")
        print(f"Marca: {self.marca}")
        print(f"Almacenamiento: {self.almacenamiento}")
        print(f"Ram: {self.ram}")
        print(f"Bateria: {self.bateria}")
        
    def encender(self):
        self.energia = int(input("Digite el valor de la carga: "))
        
        if self.energia >0:
            print(f"El celular {self.nombre} se puede encender")
            print(f"|||||||||| {self.energia} % de carga")
            print("------------------------->")
            
        else:
            print(f"El celular {self.nombre} no se puede encender")
            
    def apagar(self):
        self.off = input("Desea apagar el celular: (y/n)")
        
        if self.off == "y":
            print(f"El celular {self.nombre} se apago correctamente")
            
        else:
            print("...")
        
#creamos los objetos
objeto1=Celular("samsung","Galaxi s21","123 GB","8 GB","4500 mAh")
objeto2=Celular("Apple","iphone 12","256 GB","6 GB","4000 mAh")
objeto3=Celular("Huawei","P40 pro","512 GB","12 GB","5000 mAh")

#mostramos en consola
#print(f"Informacion del celula:{objeto1.marca}")

objeto1.encender()
objeto1.muestra_detalles()
objeto1.apagar()
#objeto2.muestra_detalles()
#objeto3.muestra_detalles()