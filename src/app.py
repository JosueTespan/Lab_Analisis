from flask import Flask
from flask_cors import CORS
from config.config import app_config

# Importa los blueprints
from apis.categoria.routes import Categoria
from apis.empresas.routes import Empresa
from apis.contactos.routes import Contactos  # 👈 Importa el blueprint de contactos

app = Flask(__name__)
CORS(app)  # Habilita CORS

if __name__ == '__main__':
    app.config.from_object(app_config['development'])

    # Registra los blueprints con sus respectivos prefijos
    app.register_blueprint(Categoria.main, url_prefix="/api/categoria")
    app.register_blueprint(Empresa.main, url_prefix="/api/empresa")
    app.register_blueprint(Contactos.main, url_prefix="/api/contacto")  # 👈 Registro para contactos

    app.run(debug=True)
