import os
from flask import Flask
from app.extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'app.db')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Bind extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    from app.main import main_bp
    from app.auth import auth_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')

    with app.app_context():
        from app import models
        db.create_all()

    return app