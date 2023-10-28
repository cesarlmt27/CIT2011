from flask import Flask, request, jsonify
import producer as p

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        data = request.form
        
        print(f"Nombre: {data['nombre']}")
        print(f"Usuario: {data['usuario']}")
        print(f"Correo: {data['correo']}")
        print(f"PAID: {data['paid']}")
        
        if data['paid']:
            p.formulario(data, 1)
        else:
            p.formulario(data, 0)

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug = True, host= "0.0.0.0")