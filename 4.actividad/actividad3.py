class Perro:
    def __init__(self, especie, edad, peso):
        # Defino los atributos de instancia de la clase
        self.especie = especie
        self.edad = edad
        self.peso = peso
    
    # Mostramos información del objeto
    def muestra_detalles(self):
        print("---------------------------->")
        print("Información del Animal")
        print("---------------------------->")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad}")
        print(f"Peso: {self.peso}")

class Gato:
    def __init__(self, especie, edad, peso, habitad, dieta):
        # Defino los atributos de instancia de la clase
        self.especie = especie
        self.edad = edad
        self.peso = peso
        self.habitad = habitad
        self.dieta = dieta
    
    # Mostramos información del objeto
    def muestra_detalles(self):
        print("---------------------------->")
        print("Información del Animal")
        print("---------------------------->")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad}")
        print(f"Peso: {self.peso}")
        print(f"Habitad: {self.habitad}")
        print(f"Dieta: {self.dieta}")

class Pajaro:
    def __init__(self, especie, edad, peso, dieta):
        # Defino los atributos de instancia de la clase
        self.especie = especie
        self.edad = edad
        self.peso = peso
        self.dieta = dieta
    
    # Mostramos información del objeto
    def muestra_detalles(self):
        print("---------------------------->")
        print("Información del Animal")
        print("---------------------------->")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad}")
        print(f"Peso: {self.peso}")
        print(f"Dieta: {self.dieta}")

# Función para mostrar la información del animal
def mostrar_informacion(animal):
    animal.muestra_detalles()

# Instancias de los animales
perro = Perro("Canino", 5, 30)
gato = Gato("Felino", 3, 8, "Casa", "Carnívoro")
pajaro = Pajaro("Ave", 2, 0.5, "Granívoro")

# Llamamos al método mostrar_informacion para cada animal
mostrar_informacion(perro)
mostrar_informacion(gato)
mostrar_informacion(pajaro)
