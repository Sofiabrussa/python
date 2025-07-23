#@staticmethod
#Un método estático es un método que pertenece a la clase, pero no recibe automáticamente ni la instancia (self) 
#ni la clase (cls) como primer argumento.
# Se usa cuando el método no necesita acceder ni a la instancia ni a la clase, pero está relacionado conceptualmente con la clase

class MiClase:
    @staticmethod
    def metodo_estatico(x, y):
        return x + y

print(MiClase.metodo_estatico(5, 7))  # Salida: 12

#--------------------------------------------------------------------------------------------------------------
#@classmethod 
# Permite acceder o modificar atributos que pertenecen a la clase (compartidos por todas las instancias).
class MiClase:
    contador = 0

    def __init__(self):
        MiClase.contador += 1

    @classmethod
    def obtener_contador(cls):
        return cls.contador

obj1 = MiClase()
obj2 = MiClase()
print(MiClase.obtener_contador()) 

#--------------------------------------------------------------------------------------------------------------
#self 
#Quiero que el método actúe sobre una instancia específica (objeto) y sus datos 
# Para acceder o modificar datos propios de ese objeto

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre  # atributo de instancia

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

p1 = Persona("Ana")
p2 = Persona("Luis")

p1.saludar()  
p2.saludar()  
