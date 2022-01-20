from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def inicio():
    return "¡Hola Mundo!"

@app.route("/dojo", methods=["GET"])
def dojo():
    return "¡Dojo!"

@app.route("/say/<palabra>", methods=["GET"])
def dicePalabra(palabra:str):
    if(palabra.isnumeric()):
        return "El parametro que está enviando debe ser una cadena"
    return f"¡Hola, {palabra.capitalize()}!"

@app.route("/repeat/<int:cantidad>/<palabra>", methods=["GET"])
def repitePalabra(cantidad:int,palabra:str):
    if(isinstance(cantidad,int)):
        return cantidad * f"{palabra} "
    else: return "El primer parametro debe ser un valor numérico"

@app.errorhandler(404)
def page_not_found(error):
    return "¡Lo siento! No hay respuesta. Inténtalo otra vez."


if( __name__ )== "__main__":
    app.run( debug=True )