class Carro:
    def __init__(self,marca,modelo,año):
        #defino los atributos de instancia de la clase
        self.marca = marca 
        self.modelo = modelo
        self.año = año

    def descripcion(self):
        print("---------------------------->")
        print("Informacion del Carro")
        print("---------------------------->")
        print(f"marca: {self.marca}")
        print(f"modelo: {self.modelo}")
        print(f"año: {self.año}")

class Moto:
    def __init__(self,marca,modelo,año,combustible):
        #defino los atributos de instancia de la clase
        self.marca = marca 
        self.modelo = modelo
        self.año = año
        self.combustible = combustible

    def descripcion(self):
        print("---------------------------->")
        print("Informacion de la moto")
        print("---------------------------->")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Combustible: {self.combustible}")

class Bicicleta:
    def __init__(self,marca,modelo,año,color):
        #defino los atributos de instancia de la clase
        self.marca = marca 
        self.modelo = modelo
        self.año = año
        self.color = color
        
    #mostramos informacion del objeto
    def descripcion(self):
        print("---------------------------->")
        print("Informacion de la Bicicleta")
        print("---------------------------->")
        print(f"marca: {self.marca}")
        print(f"modelo: {self.modelo}")
        print(f"año: {self.año}")
        print(f"color: {self.color}")

def mostrar_informacion(vehiculo):
    vehiculo.descripcion()

# Instancias de cada clase
objeto_aprendiz = Carro("Toyota","Corolla","2020")
objeto_moto = Moto("Yamaha", "MT-03", "2022","Gasolina")
objeto_bicicleta = Bicicleta("Trek", "FX 2", "2021", "Blanco")

# Llamado al método mostrar_info para cada objeto
mostrar_informacion(objeto_aprendiz)
mostrar_informacion(objeto_moto)
mostrar_informacion(objeto_bicicleta)