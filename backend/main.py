from smith import linear_diophantine_system_solver as smith_linear_diophantine_system_solver

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from sympy import Matrix

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/smith', methods=['POST'])
def smith():
    if not request.is_json:
        return jsonify({"error": "İstek JSON formatında olmalıdır."}), 400

    data = request.get_json()

    # JSON içinde gerekli anahtarların varlığını kontrol etme
    if 'matrix_2d' not in data or 'matrix_1d' not in data:
        return jsonify({"error": "JSON içinde 'matrix_2d' ve 'matrix_1d' anahtarları bulunmalıdır."}), 400

    matrix_2d = data['matrix_2d']
    matrix_1d = data['matrix_1d']

    # Matrislerin geçerli olup olmadığını kontrol etme
    if not (isinstance(matrix_2d, list) and all(isinstance(row, list) for row in matrix_2d)):
        return jsonify({"error": "'matrix_2d' iki boyutlu bir liste olmalıdır."}), 400

    if not isinstance(matrix_1d, list):
        return jsonify({"error": "'matrix_1d' tek boyutlu bir liste olmalıdır."}), 400

    try:
        sympy_matrix_2d = Matrix(matrix_2d)
        sympy_matrix_1d = Matrix(matrix_1d)

        result_matrix = smith_linear_diophantine_system_solver(sympy_matrix_2d, sympy_matrix_1d)

        # SymPy matrisini Python listesine dönüştürme
        result_list = [float(element) for element in result_matrix]

        return jsonify({"result_matrix": result_list}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/hermite', methods=['POST'])
def hermite():
    if not request.is_json:
        return jsonify({"error": "İstek JSON formatında olmalıdır."}), 400

    data = request.get_json()

    # JSON içinde gerekli anahtarların varlığını kontrol etme
    if 'matrix_2d' not in data or 'matrix_1d' not in data:
        return jsonify({"error": "JSON içinde 'matrix_2d' ve 'matrix_1d' anahtarları bulunmalıdır."}), 400

    matrix_2d = data['matrix_2d']
    matrix_1d = data['matrix_1d']

    # Matrislerin geçerli olup olmadığını kontrol etme
    if not (isinstance(matrix_2d, list) and all(isinstance(row, list) for row in matrix_2d)):
        return jsonify({"error": "'matrix_2d' iki boyutlu bir liste olmalıdır."}), 400

    if not isinstance(matrix_1d, list):
        return jsonify({"error": "'matrix_1d' tek boyutlu bir liste olmalıdır."}), 400

    try:
        sympy_matrix_2d = Matrix(matrix_2d)
        sympy_matrix_1d = Matrix(matrix_1d)

        result_matrix = smith_linear_diophantine_system_solver(sympy_matrix_2d, sympy_matrix_1d)

        # SymPy matrisini Python listesine dönüştürme
        result_list = [float(element) for element in result_matrix]

        return jsonify({"result_matrix": result_list}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
