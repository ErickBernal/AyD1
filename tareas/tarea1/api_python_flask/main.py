from flask import Flask , request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World, Tarea1!"

@app.route("/Calculadora_201480017",methods=["POST"])
def calculadora():
    post_details = request.get_json()
    n1 = post_details["n1"]
    n2 = post_details["n2"]
    return "La suma es: " + str((n1 + n2))



