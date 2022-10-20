# try: 
#     int ("a")
# except ZeroDivisionError:
#     print ("No se puede dividir entre cero")
# except ValueError:
#     print ("No se puede convertir a entero")
# except Exception as error:
#     print(error.args)
#     print("Error desconocido")
# print ("yo no soy un error")

# try:
#     raise Exception("wadafa", "xqloco", "codigolagarto")
# except Exception as error:
#     print(error.args)

# try:
#     resultado = 5/1
#     raise Exception("wadafa", "xqloco", "codigolagarto")
# except Exception as error:
#     print(error.args)
# else:
#     print("todo salio bien")
# finally:
#     print("se ejecuta siempre")



numero = input("ingrese un numero: ")
# convertir ese numero a un entero , sino se puede indicar que el valor es incorrecto). sumar 10 + ese numero ingresado y devolver

try: 
    int(numero)
except ValueError:
    print ("No se puede convertir a entero")
else:
    print(int(numero) + 10)
