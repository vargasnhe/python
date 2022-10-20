# alumnos = [
#   {
#     "id": 1,
#     "nombre": "Eduardo",
#     "dni": 76543210,
#     "status": True
#   },
#   {
#     "id": 2,
#     "nombre": "Jorge",
#     "dni": 76543354,
#     "status": True
#   },
#   {
#     "id": 3,
#     "nombre": "Raul",
#     "dni": 76543233,
#     "status": True
#   },
#   {
#     "id": 4,
#     "nombre": "Miguel",
#     "dni": 24543210,
#     "status": False
#   },
#   {
#     "id": 5,
#     "nombre": "Jose",
#     "dni": 76663210,
#     "status": False
#   }
# ]
#extraer nombre solo si el alumno esta activo
# alumnos_activos = []
# def extraerNombre(lista_alumnos):
#     for alumno in lista_alumnos:
#         if alumno["status"] == True:
#             alumnos_activos.append(alumno["nombre"])
#         else: 
#             pass
        

# extraerNombre(alumnos)
# print (alumnos_activos)

#funcion que cuente la cantidad de palabras que tiene una frase


def contarPalabras():
    frase = input("Ingresa una frase: ")
    