nombre = ["Juan", "Pedro", "Maria", "Luis", "Ana", "Rosa", "Luisa"]
miscelaneo = [1, 2, 3, 4, "Hola", "Adios", True, False]
print (nombre [3])
print(len("Hola"))
print(len(miscelaneo))
print(nombre[0:2])
print(nombre[-2])
print(nombre [0:3])
print (nombre + miscelaneo)
print (nombre [:])
print (nombre [:3]+nombre [5:])
print (nombre [5:])
alumnos=nombre
print(id(alumnos))
print (id(nombre))
nombre [0] = "Eduardo"
nombre ="hola mundo"
print (nombre)
print (id(nombre))
alumnitos = alumnos [:]
print (id(alumnitos))
alumnos.append("FRANCISCO")
print (alumnos)
alumnos.pop(0)
print(alumnos)
alumno_eliminado = alumnos.pop(0)
print(alumno_eliminado)
print (alumnos)
alumno_eliminado_2 = alumnos.remove("Luis")
print(alumnos)
print(alumno_eliminado_2)
alumnos.append("LUIS")
del alumnos[1]
print (alumnos)
alumnos.clear()
print (alumnos)

#tuplas son inmutables  no se pueden modificar  no se pueden agregar ni eliminar    
cursos = ("Python", "Django", "Flask", "Java", "C++", "C#", "PHP")
mix = ("Python", 2, 3.4, True, "Django", "Flask", "Java", "C++", "C#", "PHP")
#cursos.append("Ruby")

#del (cursos)
print (cursos)
print ((cursos[3:]))
#set
primos = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
print (primos)
primos.add(101)
print (primos)
primos.pop()
print (primos)
#diccionario
#.pop() elimina el ultimo elemento
#una colección de datos que se almacenan en pares de llave:valor

persona = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 28,
    "cursos": ["Python", "Django", "Flask", "Java", "C++", "C#", "PHP"],
    "telefono": "123456789",

}
print (persona["nombre"])
print (persona.get("direccion", "No existe"))

print (persona.keys())
print (persona.values())
persona["direccion"] = "Av. Siempre Viva 123"
print (persona["direccion"])
cutsos_eliminado= persona.pop ("cursos")
print (cutsos_eliminado)
print (persona)

#listas ordenadas y editables
#tuplas ordenadas e inmutables
#set no ordenados y no indexados
#diccionarios no ordenados, indexados y editables

