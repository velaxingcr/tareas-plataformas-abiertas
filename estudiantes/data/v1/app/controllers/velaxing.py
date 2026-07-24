from flask import Blueprint, request, jsonify

# Crear el Blueprint
velaxing_endpoints = Blueprint("velaxing_endpoints", __name__)


# Endpoint 1
@velaxing_endpoints.route("/hola", methods=["GET"])
def hola():
    return jsonify({
        "mensaje": "¡Bienvenido a Velaxing! Donde cada vela ilumina momentos especiales."
    }), 200


# Endpoint 2
@velaxing_endpoints.route("/saludo", methods=["GET"])
def saludo():

    nombre = request.args.get("nombre")

    if not nombre:
        return jsonify({
            "error": "Debe de ingresar el nombre del estudiante."
        }), 400

    return jsonify({
        "saludo": f"¡Hola {nombre}! Bienvenido a Velaxing."
    }), 200


# Endpoint 3: listar todas las velas
@velaxing_endpoints.route("/velas", methods=["GET"])
def listar_velas():
    velas = [
        {
            "nombre": "Serenity Lavanda",
            "aroma": "Lavanda",
            "tamano": "Mediana",
            "descripcion": "Vela aromática con esencia relajante de lavanda.",
            "precio": 6500,
            "moneda": "CRC",
            "stock": 12
        },
        {
            "nombre": "Dulce Vainilla",
            "aroma": "Vainilla",
            "tamano": "Grande",
            "descripcion": "Vela aromática con una fragancia dulce y cremosa.",
            "precio": 8500,
            "moneda": "CRC",
            "stock": 8
        },
        {
            "nombre": "Canela & Especias",
            "aroma": "Canela",
            "tamano": "Mediana",
            "descripcion": "Vela de aroma cálido con notas de canela y especias.",
            "precio": 7000,
            "moneda": "CRC",
            "stock": 10
        }
    ]

    return jsonify(velas), 200
