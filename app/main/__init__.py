from flask import Blueprint

# Define blueprint named 'main'
main_bp = Blueprint('main', __name__)

from app.main import routes