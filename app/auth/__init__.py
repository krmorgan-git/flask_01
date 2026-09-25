from flask import Blueprint

# Define blueprint named 'auth'
auth_bp = Blueprint('auth', __name__)

from app.auth import routes