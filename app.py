from flask import Flask, request, jsonify, render_template
from entities.ciudad import Ciudad

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rastreo')
def rastreo():
    return render_template('rastreo.html', rastreo= rastreo)

@app.route('/envios', methods=['GET'])
def get_envios():
    envios = Ciudad.get_envios()
    return render_template('envios.html', envios = envios)



@app.route('/ciudades')
def ciudades():
    ciudades = Ciudad.get_all()
    return render_template('ciudades.html', ciudades = ciudades)

@app.route('/ciudad-registro', methods=['GET'])
def ciudad_registro():
    return render_template('ciudad.html')

@app.route('/ciudad', methods=['GET'])
def get_ciudades():
    ciudades = Ciudad.get_all()
    return jsonify(ciudades), 200

@app.route('/ciudad', methods=['POST'])
def save():
    data = request.json
    ciudad = Ciudad(nombre=data['nombre'], codigo=data['codigo'])
    id = Ciudad.save(ciudad)
    return jsonify({'id' : id}), 201

@app.route('/ciudad/<int:id>', methods=['PUT'])
def update(id):
    data = request.json
    ciudad = Ciudad(nombre=data['nombre'], codigo=data['codigo'])
    result = Ciudad.update(id, ciudad)
    if result == 0:
        return jsonify({'error': 'El registro de ciudad no existe'}), 404
    return jsonify({'id': id}), 201

@app.route("/ciudad/eliminar/<int:id>", methods=["DELETE"])
def eliminar_ciudad(id):
    try:
        resultado = Ciudad.delete(id)
        if resultado > 0:
            return jsonify({"message": "Ciudad eliminada exitosamente"}), 200
        else:
            return (
                jsonify({"error": "No se encontró la ciudad con el ID proporcionado"}),
                404,
            )
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()