class Persona:
    estatura = 1.55
    peso = 300
    signo = "Aries"
    
#magic method __al inicio y al final del nombre del metodo__ 

    def __str__(self):
        #str es un metodo magico que se ejecuta cuando se imprime un objeto
        return "Bienvenido a la clase Persona"
    def saludar(self):
        texto = print("Hola, soy una persona y mido") + str(self.estatura)
        print (texto)
    def saludar_cordialmente(self, nombre):
        texto = "hola {} mucho gusto".format(nombre)
        print(texto)
# variable > instancia de la clase
eduardo = Persona()
gabriela = Persona()

print (eduardo)

eduardo.estatura= 1.80
gabriela.estatura= 1.60

print(eduardo.estatura)
print(gabriela.estatura)

eduardo.saludar_cordialmente("Gurrumino")
resultado = eduardo.saludar_cordialmente("Andres")
# eduardo.saludar()
# gabriela.saludar()
print(resultado)