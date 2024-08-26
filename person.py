# tarea hacer una clase persona
class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    def datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Sexo:", self.sexo)

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {self.sexo}"

# Ejemplo de uso
persona1 = Persona("Juan", 30, "Masculino")
persona2 = Persona("Maria", 25, "Femenino")
persona3 = Persona("Pedro", 40, "Masculino")

print(persona1)
print(persona2)
print(persona3)
