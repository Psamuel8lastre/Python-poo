class Personas:
    
    def __init__(self,nombres,apellidos,identidad,fechanacimiento,sexo):
        self.__nombres=nombres
        self.__apellidos=apellidos
        self.__identidad=identidad
        self.fechanacimiento=fechanacimiento
        self.sexo=sexo
        
        #metodo getter
    def obtener_nombre(self):
        return self.__nombres
    
    def obtener_apellidos(self):
        return self.__apellidos
    
    def obtener_identidad(self):
        return self.__identidad
    
    #metodo setter
    def establecer_nombres(self, nuevo_nombre):
        self.__nombres=nuevo_nombre
        
    def establecer_apellidos(self, nuevo_apellidos):
        self.__apellidos=nuevo_apellidos
        
        
    
    #este metodo muestra detalles del objeto
    def mostrar_detalles(self):
        print(f"||||||||||||||||||||")
        print(f"\nNombres: {self.__nombres}")
        print(f"Apellidos: {self.__apellidos}")
        print(f"N° identidad: {self.__identidad}")
        print(f"Fecha de nacimiento: {self.fechanacimiento}")
        print(f"Sexo: {self.sexo}")
        
#objeto
persona=Personas("Daniel","Buelvas",1102345762,"31/10/2004","M")

#Imprimir atributos publicos y privados
persona.mostrar_detalles()

print("||||||||||||||||||||||")

#se imprimen los atributos encapsulados y modificados
persona.establecer_nombres("Samuel")
print(f"Nombres: { persona.obtener_nombre() }")
persona.establecer_apellidos("Lastre")
print(f"Apellidos: { persona.obtener_apellidos() }")
print(f"N° identidad: { persona.obtener_identidad() }")
print(f"Fecha de nacimiento: { persona.fechanacimiento }")
print(f"Sexo: { persona.sexo }")