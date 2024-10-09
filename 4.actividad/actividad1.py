class Aprendiz:
    def __init__(self, nombres, apellidos, cedula, sexo):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.sexo = sexo
        self.formacion = input("Programa de formación: ")
        self.regional = input("Regional: ")

    def mostrar_info(self):
        print("Hola, soy un aprendiz SENA")
        print(f"Nombre: {self.nombres} {self.apellidos}")
        print(f"CC: {self.cedula}")
        print(f"Estudiante del programa: {self.formacion} de la Regional {self.regional}")

class Instructor:
    def __init__(self, nombres, apellidos, cedula, area):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.area = area

    def mostrar_info(self):
        print("Hola, soy un instructor del SENA")
        print(f"Nombre: {self.nombres} {self.apellidos}")
        print(f"CC: {self.cedula}")
        print(f"Área de instrucción: {self.area}")

class Coordinador:
    def __init__(self, nombres, apellidos, cedula, departamento):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.departamento = departamento

    def mostrar_info(self):
        print("Hola, soy un coordinador del SENA")
        print(f"Nombre: {self.nombres} {self.apellidos}")
        print(f"CC: {self.cedula}")
        print(f"Departamento: {self.departamento}")

def mostrar_informacion(persona):
    persona.mostrar_info()

# Instancias de cada clase
objeto_aprendiz = Aprendiz("Samuel Elias", "Vega Barrios", 123456789, "Masculino")
objeto_instructor = Instructor("Laura", "Rodriguez", 987654321, "Programación")
objeto_coordinador = Coordinador("Carlos", "Martinez", 123456789, "Recursos Humanos")

# Llamado al método mostrar_info para cada objeto
mostrar_informacion(objeto_aprendiz)
mostrar_informacion(objeto_instructor)
mostrar_informacion(objeto_coordinador)