"""
APIのルート定義を行うモジュール
"""
from flask import Blueprint, request, jsonify

from calc_api.operations import add, subtract, multiply, divide, CalculationError
from calc_api.validation import validate_numeric_params, ValidationError

# Blueprintの作成
calc_bp = Blueprint('calc', __name__)


@calc_bp.route('/add', methods=['GET'])
def add_route():
    """加算のエンドポイント"""
    try:
        params = validate_numeric_params(request.args)
        result = add(params['a'], params['b'])
        return jsonify({"result": result})
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400


@calc_bp.route('/subtract', methods=['GET'])
def subtract_route():
    """減算のエンドポイント"""
    try:
        params = validate_numeric_params(request.args)
        result = subtract(params['a'], params['b'])
        return jsonify({"result": result})
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400


@calc_bp.route('/multiply', methods=['GET'])
def multiply_route():
    """乗算のエンドポイント"""
    try:
        params = validate_numeric_params(request.args)
        result = multiply(params['a'], params['b'])
        return jsonify({"result": result})
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400
    except IndexError:
        return jsonify({"error": "An unexpected error occurred with negative multiplier."}), 500


@calc_bp.route('/divide', methods=['GET'])
def divide_route():
    """除算のエンドポイント"""
    try:
        params = validate_numeric_params(request.args)
        result = divide(params['a'], params['b'])
        return jsonify({"result": result})
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400
    except CalculationError as e:
        return jsonify({"error": str(e)}), 400


@calc_bp.route('/', methods=['GET'])
def index():
    """APIの使用方法を説明するエンドポイント"""
    return jsonify({
        "name": "Calculator API",
        "endpoints": {
            "/add": "Add two numbers: /add?a=1&b=2",
            "/subtract": "Subtract b from a: /subtract?a=5&b=3",
            "/multiply": "Multiply two numbers: /multiply?a=4&b=5",
            "/divide": "Divide a by b: /divide?a=10&b=2"
        },
        "note": "All parameters should be numbers. Division by zero is not allowed."
    })