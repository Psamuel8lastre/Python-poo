class Instrumento:
    # Método constructor
    def __init__(self, instrumento, marca, material):
        # Defino los atributos de instancia de la clase
        self.instrumento = instrumento
        self.marca = marca
        self.material = material   # Eliminé la 'q' que estaba causando error
        
        self.precio = int(input("Ingrese el precio del instrumento: "))
        
    # Método para mostrar la información del objeto
    def registro(self):
        print("---------------------------->")
        print("Instrumentos registrados")
        print("---------------------------->")
        print(f"Instrumento: {self.instrumento}")
        print(f"Marca: {self.marca}")
        print(f"Material: {self.material}")
        print(f"Precio del instrumento: {self.precio} pesos")

        
class Guitarra(Instrumento):
    def __init__(self, instrumento, marca, material):
        super().__init__(instrumento, marca, material)
        
        # Definir el sistema operativo y conectividad
        self.ndecuerdas = input("Ingrese el numero de cuerdas: ")
        self.acordesBasicos = input("Ingrese acordes: (separelos con comas porfa)")
        
    def tocarinstrumento(self):
        self.tocar = input("Desea tocar el instrumento (Y/N): ")
        
        if self.tocar.lower() == "y":
            print(f"||||||||||")
            print(f"Tocando acordes {self.acordesBasicos} ")
            print("------------------------->")
        else:
            print("...")
            

            
# Crear el objeto de la clase Smartphone
objeto_musica = Guitarra("guitarra", "Yamaha", "Madera")
objeto_musica.registro()
objeto_musica.tocarinstrumento()
