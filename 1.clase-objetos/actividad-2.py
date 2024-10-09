#creo la clase
class Animal:
    #metodo constructor
    def __init__(self,especie,edad,peso,habitad,dieta):
        #defino los atributos de instancia de la clase
        self.especie = especie 
        self.edad = edad
        self.peso = peso
        self.habitad = habitad
        self.dieta = dieta
        
    #mostramos informacion del objeto
    def muestra_detalles(self):
        print("---------------------------->")
        print("Informacion del Animal")
        print("---------------------------->")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad}")
        print(f"Peso: {self.peso}")
        print(f"Habitad: {self.habitad}")
        print(f"Dieta: {self.dieta}")
        
    def comer(self):
        self.alimentar = input("Desea alimentar el animal: (y/n)")
        
        if self.alimentar == "y":
            print(f"El  {self.especie} se alimento correctamente ;3")
            
        else:
            print(":(")
    def dormir(self):
        self.descansar = input("Desea que el animal duerma: (y/n)")
        
        if self.descansar == "y":
            print(f"El  {self.especie} esta descansando ;3")
            
        else:
            print("...")
        
objeto1=Animal("leon","18 años","10 kg","sabana","carnivoro")
objeto2=Animal("Elefante","15 años","5400 kg","selva","Hervivoro")
objeto3=Animal("Gato","3 años","4 kg","hogar","omnivoro")


objeto1.muestra_detalles()
objeto1.comer()
objeto1.dormir()
#objeto2.muestra_detalles()
#objeto3.muestra_detalles()