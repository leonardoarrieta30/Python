
from select import select
from tkinter import Variable


def diccionarios():
    Personas={
        "Nombre":"Leonardo Santos Arriera Huaman",
        "Edad":20,
        "Direccion":"Calle rio majes 246",
        "Telefono":912617842,
        "ganador":True,
        "Pago":[3500,4200,4100]

    }
    car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }

    print(Personas.keys()) #llaves,claves
    print(Personas.values())# muestra los valores en forma ordenada del diccionario
    print(Personas.items()) #muestra una los items del diccionario en listas dentro de tuplas


# class Persona:
#     idx=1

#     def __init__(self,nombre,edad):
#         self.nombre=nombre
#         self.edad=edad

#     def hablar(self,mensaje):
#         print(mensaje)

# p1=Persona("Leonardo",20)
# p1.hablar("Hola")
# print("El nombre es: ",p1.nombre,"y su edad es: ",p1.edad)



class Coche:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.arrancado = False
    def arrancar(self):
        self.arrancado=True
        print("El",self.marca,self.modelo,"se ha arrancado")
    def parar(self):
        self.arrancado=False
        print("El",self.marca,self.modelo,"se ha parado")

coche1=Coche("Samsung","C740")
coche2=Coche("Daewoo","Cja1")

print("La marca del coche 1 es: "+coche1.marca," y su modelo es: "+coche1.modelo)
print("La marca del coche 2 es: "+coche2.marca," y su modelo es: "+coche2.modelo)

print(coche1.arrancado)
print(coche2.arrancado)
coche1.arrancar()
coche2.arrancar()
print(coche1.arrancado)
print(coche2.arrancado)
coche1.parar()
coche2.parar()
print(coche1.arrancado)
print(coche2.arrancado)