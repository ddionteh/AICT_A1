from flask import Blueprint

# Import all route modules
from .route_planning import route_planning
from .logic_inference import logic_inference
from .bayesian_network import bayesian_network
from .optimisation import optimisation

# Create a blueprint for routes (optional if registering in `app/__init__.py`)
routes_bp = Blueprint('routes', __name__)

# Register blueprints inside routes_bp if needed
routes_bp.register_blueprint(route_planning)
routes_bp.register_blueprint(logic_inference)
routes_bp.register_blueprint(bayesian_network)
routes_bp.register_blueprint(optimisation)

# Expose routes for external imports
__all__ = ["route_planning", "logic_inference", "bayesian_network", "optimisation"]
