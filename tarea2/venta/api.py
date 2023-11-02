from flask import Flask, request, jsonify
import producer as p
import producer as p
import time
import metricas as m

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        data = request.form
        
        tiempo_inicio = time.time() # Registrar el tiempo de inicio
        m.tiempo_inicio_list.append(tiempo_inicio)
        
        print(f"Usuario: {data['usuario']}")
        print(f"Monto: {data['monto']}")
        
        p.venta(data)

    return jsonify(data)


@app.route('/salir', methods=['POST'])
def salir():
    if request.method == 'POST':
        print("Petición recibida.")
        
        m.escribir_json()
        
        print("Ejecución completada.")
    return ""


if __name__ == '__main__':
    app.run(debug = True, host= "0.0.0.0")