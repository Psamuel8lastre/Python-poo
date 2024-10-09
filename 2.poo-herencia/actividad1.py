class Electrodomestico:
    #metodo constructor
    def __init__(self,marca,color,capacidad):
        #defino los atributos de instancia de la clase
        self.marca = marca 
        self.color = color
        self.capacidad = capacidad
        self.consumoelectrico = int(input("Ingrese el consumo electrico: "))
        
    #mostramos informacion del objeto
    def registro(self):
        print("---------------------------->")
        print("Electrodomesticos registrados")
        print("---------------------------->")
        print(f"Marca: {self.marca}")
        print(f"Color: {self.color}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Electricidad consumida: {self.consumoelectrico}  KWh")
        
class Refrigerador(Electrodomestico):
    def __init__(self,marca,color,capacidad,tipo):
        super().__init__(marca,color,capacidad)
        
        self.tipo = tipo
        self.temperatura = int(input("Ingrese temperatura del refrigerador: "))
        
    def ajtemperatura(self):
        print("---------------------------->")

        if self.temperatura > 2 and self.temperatura <= 6:
            print(f"Temperatura ideal de la nevera {self.temperatura}° en el frigorífico")
        else:
            print("Revisa la temperatura porfa")
            
            
nevera1_refrigeraor=Refrigerador("Frigidaire","Rojo","Grande","Refrigerador de dos puertas (Bottom Freezer)")
nevera1_refrigeraor.registro()
nevera1_refrigeraor.ajtemperatura()