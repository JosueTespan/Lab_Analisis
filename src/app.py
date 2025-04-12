from flask import Flask
from flask_cors import CORS
from config.config import app_config

# Importa los blueprints
from apis.categoria.routes import Categoria
from apis.empresas.routes import Empresa
from apis.contactos.routes import Contactos 
from apis.direcciones.routes import Direcciones
from apis.emails.routes import Emails
from apis.historial.routes import Historial
from apis.recordatorios.routes import Recordatorios
from apis.notas.routes import Notas
from apis.telefonos.routes import Telefonos
from apis.notificaciones.routes import Notificaciones

app = Flask(__name__)
CORS(app) 

app.config.from_object(app_config['development'])

app.register_blueprint(Categoria.main, url_prefix="/api/categoria")
app.register_blueprint(Empresa.main, url_prefix="/api/empresa")
app.register_blueprint(Contactos.main, url_prefix="/api/contacto")  
app.register_blueprint(Direcciones.main, url_prefix="/api/direccion")
app.register_blueprint(Emails.main, url_prefix="/api/emails")
app.register_blueprint(Historial.main, url_prefix="/api/historial")
app.register_blueprint(Recordatorios.main, url_prefix="/api/recordatorio")
app.register_blueprint(Notas.main, url_prefix="/api/nota")
app.register_blueprint(Telefonos.main, url_prefix="/api/telefono")
app.register_blueprint(Notificaciones.main, url_prefix="/api/notificacion")

if __name__ == '__main__':
    app.run(debug=True)
