from flask import Flask, request

app = Flask(__name__)

# ruta donde queremos que se corra la funcion
@app.route('/')
def hello():
    # Obtenemos la ip del usuario
    user_ip = request.remote_addr
    return 'Hola tu ip es {}'.format(user_ip)
