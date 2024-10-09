from abc import ABC, abstractmethod
import math

class Empleado (ABC):
    @abstractmethod
    def calcular_salario(self):
        pass
    
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre,salarioMensual):
        self.nombre = nombre
        self.salarioMensual = salarioMensual
        
    def calcular_salario(self):
        return self.salarioMensual
    
class EmpleadoPorHoras (Empleado):
    def __init__(self, nombre,salarioporHora):
        self.nombre = nombre
        self.salarioporHora = salarioporHora
        
    def calcular_salario(self):
        return self.salarioporHora
    
    
empleado1 = EmpleadoTiempoCompleto("samuel", 1500000)
print(f"El salario del empleado1 es: {empleado1.calcular_salario()}")

empleado2 = EmpleadoPorHoras ("daniel",4900)
print(f"El salario del empleado2 es: {empleado2.calcular_salario()}")