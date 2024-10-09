class Reloj:
    # Método constructor
    def __init__(self, marca, tipo, material):
        # Defino los atributos de instancia de la clase
        self.marca = marca 
        self.tipo = tipo
        self.material = material  
        
        self.precio = int(input("Ingrese el precio del instrumento: "))
        
    # Método para mostrar la información del objeto
    def registro(self):
        print("---------------------------->")
        print("Dispositivos registrados")
        print("---------------------------->")
        print(f"Marca: {self.marca}")
        print(f"Tipo: {self.tipo}")
        print(f"Material: {self.material}")
        print(f"Precio del reloj: {self.precio} pesos")

        
class Relojinteligente(Reloj):
    def __init__(self, marca, tipo, material):
        super().__init__(marca, tipo, material)
        
        self.tipopantalla = input("Ingrese el tipo de pantalla: ")
        self.sistemaoperativo = input("Ingrese el sistema operativo: ")
        
    def encender(self):
        self.tocar = input("Desea tocar el instrumento (Y/N): ")
        
        if self.tocar.lower() == "y":
            print(f"||||||||||")
            print(f"el reloj {self.marca} encendio correctamente")
            print("------------------------->")
        else:
            print("...")

            
# Crear el objeto de la clase Smartphone
objeto_reloj = Relojinteligente("Apple", "SmartWatch", "acero")
objeto_reloj.registro()
objeto_reloj.encender()
