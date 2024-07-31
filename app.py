from flask import Flask
from config import Config
from models import db
from routes import routes_blueprint
# from dashboard import dashboard as dashboard_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar o banco de dados
    db.init_app(app)

    # Registre os blueprints para rotas e dashboard
    app.register_blueprint(routes_blueprint)

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        # Cria as tabelas no banco de dados se não existirem
        db.create_all()
    app.run(debug=True)
