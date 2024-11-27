from flask import Flask, request, jsonify, render_template
from entities.ciudad import Ciudad

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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

if __name__ == '__main__':
    app.run()