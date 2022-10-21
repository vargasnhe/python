class Usuario:
    def __init__(self, nombre, apellido, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
    def mostrar_resumen(self):
        return { {self.nombre,self.apellido,self.correo}
    }
    
class Alumno(Usuario):
    def __init__(self, nombre, apellido, correo, telefono):
        self.telefono=telefono
        super().__init__(nombre, apellido, correo)
    def saludar(self):
        print ("Hola soy un alumno")
    def mostrar_resumen(self):
        resumen = super().mostrar_resumen()
        resumen["telefono"]= self.telefono
        return resumen 
usuario01 = Usuario("Eduardo", "Rivero", "eduardorivero@gmail.com")
usuario02 = Usuario("Julissa", "Perez", "julissaperez@gmail.com")
usuario03 = Usuario("Franco", "Portugal", "francoportugal@gmail.com")


