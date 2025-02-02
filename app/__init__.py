from flask import Flask
from app.db.db import db
from app.config.config import get_config_by_name  # ✅ Import the config function
from app.routes.route_planning import route_planning
from app.routes.logic_inference import logic_inference
from app.routes.bayesian_network import bayesian_network
from app.routes.optimisation import optimisation
from app.routes.main import main  # ✅ Serves frontend

def create_app(config_name='development'):  # ✅ Accept config_name argument
    app = Flask(__name__)

    # ✅ Load Configuration
    app.config.from_object(get_config_by_name(config_name))

    # ✅ Initialize Database
    db.init_app(app)

    # ✅ Register Blueprints
    app.register_blueprint(route_planning)
    app.register_blueprint(logic_inference)
    app.register_blueprint(bayesian_network)
    app.register_blueprint(optimisation)
    app.register_blueprint(main)

    return app
