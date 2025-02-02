from flask import Blueprint, jsonify

logic_inference = Blueprint('logic_inference', __name__, url_prefix="/api/logic")

@logic_inference.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Logic Inference API is working!"})
