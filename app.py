from flask import Flask
from config import Config
from models.producto_model import db
from controllers.producto_controller import producto_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()   # Crea la tabla si no existe

    app.register_blueprint(producto_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
