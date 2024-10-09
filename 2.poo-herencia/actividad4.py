class Electronico:
    # Método constructor
    def __init__(self, marca, modelo, procesador):
        # Defino los atributos de instancia de la clase
        self.marca = marca 
        self.modelo = modelo
        self.procesador = procesador  
        
        self.RAM = int(input("Ingrese memoria RAM: "))
        
    # Método para mostrar la información del objeto
    def registro(self):
        print("---------------------------->")
        print("Dispositivos registrados")
        print("---------------------------->")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Tipo de procesador: {self.procesador}")
        print(f"Memoria RAM: {self.RAM} GB")

        
class Laptop(Electronico):
    def __init__(self, marca, modelo, procesador):
        super().__init__(marca, modelo, procesador)
        
        self.tipodiscoDuro = input("Ingrese el tipo de disco duro: ")
        self.duracionbateria = input("Ingrese la duracion de la bateria: ")
        
    def encender(self):
        self.tocar = input("Desea tocar el instrumento (Y/N): ")
        
        if self.tocar.lower() == "y":
            print(f"||||||||||")
            print(f"el laptop {self.marca} encendio correctamente")
            print("------------------------->")
        else:
            print("...")

            
# Crear el objeto de la clase Smartphone
objeto_computador = Laptop("hp", "pavilion", "2023")
objeto_computador.registro()
objeto_computador.encender()
