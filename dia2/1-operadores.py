numero1, numero2 = 10, 50
#suma
print("La suma de", numero1, "y", numero2, "es", numero1 + numero2)
#resta
print ("La resta de", numero1, "y", numero2, "es", numero1 - numero2)
#multiplicacion
print("La multiplicacion de", numero1, "y", numero2, "es", numero1 * numero2)
print("hola"*5)
#division
print( "La division de", numero1, "y", numero2, "es", numero1 / numero2)
#modulo
print("El modulo de", numero1, "y", numero2, "es", numero1 % numero2)
#cociente
print("El cociente de", numero1, "y", numero2, "es", numero1 // numero2)
#exponente
print("El exponente de", numero1, "y", numero2, "es", numero1 ** numero2)

#operadores de asignacion
#igual
numero1 = 100
#incremento
numero1 += 1
print(numero1)
#decremento
numero1 -= 1
#multiplicacion
numero1 *= 2
#division
numero1 /= 5
print(numero1)
print (numero2) 
print (numero1 == numero2)
print (int (40.23)  ) #convierte a entero
print (type(numero1)==type(numero2)) #compara el tipo de dato
print (numero1>numero2) #compara si es mayor
print (numero1<numero2) #compara si es menor
print (100>= float("40.245")) #compara si es mayor o igual
print (40==  int(float("40.245"))) #compara si es mayor o igual
#operadores logicos
#and or xor not     #and y, or o, xor o exclusivo, not no
eduardo, ronald, henry, carmen, angel = 20, 30, 40, 50, 60
print (eduardo < ronald and ronald < henry and henry < carmen and carmen < angel)
print (eduardo > ronald or ronald > henry or henry > carmen or carmen < angel or angel < 70)
#operadores de contenido
verduras = ["lechuga", "cebolla", "tomate", "zanahoria", "brocoli"]
print ("lechuga" in verduras)
print ("lechuga" not in verduras)
