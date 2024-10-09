#creo la clase
class Empleado:
    #metodo constructor
    def __init__(self,nombre,edad,puesto,salario,añosServicio):
        #defino los atributos de instancia de la clase
        self.nombre = nombre 
        self.edad = edad
        self.puesto = puesto
        self.salario = salario
        self.añosServicio = añosServicio
        
    #mostramos informacion del objeto
    def muestra_detalles(self):
        print("---------------------------->")
        print("Informacion del Empleado")
        print("---------------------------->")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Puesto: {self.puesto}")
        print(f"Salario: {self.salario}")
        print(f"Años de servicio: {self.añosServicio}")
        
    def comer(self):
        self.alimentar = input("Desea que el emplead@ coma: (y/n)")
        
        if self.alimentar == "y":
            print(f"{self.nombre} se alimento correctamente ;3")
            
        else:
            print(":(")
    def dormir(self):
        self.descansar = input("Desea que el emplead@ duerma: (y/n)")
        
        if self.descansar == "y":
            print(f"{self.nombre} esta descansando ;3")
            
        else:
            print("...")
        
objeto1=Empleado("Juan","35 años","Ingeniero en sistemas","600,000","4 años")
objeto2=Empleado("Laura","28 años","Contadora","450,000","6 años")
objeto3=Empleado("Carlos","50 años","Gerente de ventas","700,000","10 años")


objeto1.muestra_detalles()
objeto1.comer()
objeto1.dormir()
#objeto2.muestra_detalles()
#objeto3.muestra_detalles()