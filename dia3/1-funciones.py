from tkinter import N


def miFuncion ():
     print ("Hola Mundo")
def suma(a, b):
    return a**2 + b**2 + 2*a*b
# miFuncion()
# print (suma(2, 3))

# edad = int(input("Ingresa tu edad: "))
# def comprobarEdad(edad):
#     if (edad >= 18):
#         return "Eres mayor de edad"
#     else: 
#         return "Eres menor de edad, no puedes ingresar"
# print(comprobarEdad(edad))

# genero = input("Ingresa tu genero: ")  
# def comprobarGenero(genero):
#     if (genero == "M" or genero == "m"):
#         return "Eres hombre"
#     elif (genero == "F" or genero == "f"):
#         return "Eres mujer"
#     else: 
#         return "eres o no eres"
# print(comprobarGenero(genero))

# alumnos = ["Juan", "Pedro", "Maria", "Luis", "Ana"]
# def alumnoExiste():
#         if not "Juan" in alumnos:
#             return "No existe"
#         return "Si existe"
# print(alumnoExiste())

#ingresar lista de nombres y que funcion haga la busqueda del ultimo nombre

nombres = []
# nombres.append(input("Ingresa el primer nombre: "))
# nombres.append(input("Ingresa el segundo nombre: "))
# nombres.append(input("Ingresa el tercer nombre: "))
# nombres.append(input("Ingresa el cuarto nombre: "))
# def buscarUltimoNombre():
#     return nombres[-1] 
# print (" el ultimo nombre es " ,buscarUltimoNombre())

nombres.extend(input("Ingresa los nombres separados con espacios: ").split(" "))
nombre_a_buscar = input("Ingresa el nombre a buscar: ")
def buscarPersona (nombre):
    if nombre in nombres:
        return "{} si esta en la lista {}".format(nombre, "😄")
    return "{} no esta en la lista {} ".format(nombre, "🥶")
print (buscarPersona(nombre_a_buscar))

