from flask import Flask, request
from datetime import datetime
from flask_cors import CORS
print(__name__)
app=Flask(__name__)
CORS(app)
usuarios = [ {
    "correo": "correo@gmail.com",
    "nombre": "Juan ",
    "apellido": "Perez"
} ]

@app.route('/', methods=['GET'])
def inicio():
    print("ingrese endopoint inicial")
    return "bienvenidos a mi primera api en flask semana2"
 

@app.route('/estado', methods=['GET'])
def estado():
    hora_servidor = datetime.now().strftime("%Y:%m:%d %I:%M:%S %p")
    return {'estado':True,
            "hora":hora_servidor
            }

@app.route("/registrarse", methods=['POST'])
def registro():
    print(request.data)
    print(request.get_json()) 
    body = request.get_json()
    
    for usuario in usuarios:
        print(usuario)  
    
    correo= usuario.get("correo")
    if correo == body.get("correo"):
        return {"mensaje":"usuario ya esta registrado"}
    
    # body.get("correo")
    # body ["correo"]
    usuarios.append(body)
    return {"mensaje":"usuario registrado exitosamente"}

@app.route("/listar", methods=['GET'])
def listar():
    return {
        "mensaje":"listado de usuarios",
        "content":usuarios
    }



app.run(debug=True)
