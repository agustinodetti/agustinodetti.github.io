from flask import Flask, request, jsonify

app = Flask(__name__)

# Ejemplo de una función Python que deseas ejecutar
@app.route('/run_code', methods=['POST'])
def run_code():
    # Obtener datos enviados desde el front-end si es necesario
    data = request.json
    # Ejecutar tu código Python aquí
    resultado = "Hola, este es el resultado de mi código Python"

    # Puedes hacer cualquier procesamiento que necesites aquí
    # Por ejemplo, si `data` contiene alguna información, podrías usarla en el cálculo

    # Devuelve el resultado al front-end como JSON
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)