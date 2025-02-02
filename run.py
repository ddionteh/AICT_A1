import os
from dotenv import load_dotenv
from app import create_app, db
from app.models import *  # Import models

# ✅ Load environment variables
load_dotenv()
config_name = os.getenv('FLASK_ENV', 'development')  # ✅ Default to 'development'

app = create_app(config_name)  # ✅ Pass config name

# ✅ Create database tables if they don’t exist
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    if config_name == 'development':
        app.run(debug=True)
    else:
        from werkzeug.serving import run_simple
        run_simple('0.0.0.0', 5000, app)
