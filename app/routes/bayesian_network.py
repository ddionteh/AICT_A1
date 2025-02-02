from flask import Blueprint, jsonify

bayesian_network = Blueprint('bayesian_network', __name__, url_prefix="/api/bayesian")

@bayesian_network.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Bayesian Network API is working!"})
