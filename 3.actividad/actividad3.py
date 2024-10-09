class Libro:
    
    def __init__(self,titulo,autor,isbn,editorial ):
        self.__titulo=titulo
        self.__autor=autor
        self.__isbn=isbn
        self.editorial =editorial 

        
        #metodo getter
    def obtener_titulo(self):
        return self.__titulo
    
    def obtener_autor(self):
        return self.__autor
    
    def obtener_isbn(self):
        return self.__isbn
    
    #metodo setter
    def establecer_titulos(self, nuevo_titulo):
        self.__titulo=nuevo_titulo
        
    def establecer_autores(self, nuevo_autor):
        self.__autor=nuevo_autor
        
    def establecer_isbn(self, nuevo_isbn):
        self.__isbn=nuevo_isbn
    
    #este metodo muestra detalles del objeto
    def mostrar_detalles(self):
        print(f"||||||||||||||||||||")
        print(f"\nTitulo: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"ISBN: {self.__isbn}")
        print(f"Editorial: {self.editorial}")
        
#objeto
libros=Libro("Cien años de soledad","Gabriel García Márquez", 9780307474728,"Vintage Español (Penguin Random House)")

#Imprimir atributos publicos y privados
libros.mostrar_detalles()

print("||||||||||||||||||||||")

#se imprimen los atributos encapsulados y modificados
libros.establecer_titulos("La sombra del viento")
print(f"Titulo: { libros.obtener_titulo() }")
libros.establecer_autores("Carlos Ruiz Zafón")
print(f"Autor: { libros.obtener_autor() }")
libros.establecer_isbn("978 0307454898")
print(f"ISBN: { libros.obtener_isbn() }")
print(f"Editorial: { libros.editorial }")
