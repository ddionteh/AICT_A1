from flask import Blueprint, render_template, request, jsonify

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET"])
def index():
    if request.headers.get("Accept") == "application/json":
        return jsonify({"data": {"message": "Hello, World!"}})
    return render_template("index.html")

