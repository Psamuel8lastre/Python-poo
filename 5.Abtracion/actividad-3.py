from abc import ABC, abstractmethod


class TareaEmpleado (ABC):
    @abstractmethod
    def realizar_tarea(self):
        pass
    
class Ingeniero (TareaEmpleado):
    def __init__(self, nombre,tarea):
        self.nombre = nombre
        self.tarea = tarea
        
    def realizar_tarea(self):
        return self.tarea
    
class Doctor (TareaEmpleado):
    def __init__(self, nombre,tarea):
        self.nombre = nombre
        self.tarea = tarea        
    def realizar_tarea(self):
        return self.tarea
    
    
empleado1 = Ingeniero ("samuel","arreglar maquinas (3)")
print(f"La tarea fue resuelta con exito: {empleado1.realizar_tarea()}")

empleado2 = Doctor  ("Daniel","5 cirugias pendientes")
print(f"La tarea fue resuelta con exito: {empleado2.realizar_tarea()}")