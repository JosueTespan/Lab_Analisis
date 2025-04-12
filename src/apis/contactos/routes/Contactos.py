from flask import Blueprint, jsonify, request
import uuid
from ..models.ContactosModels import ContactoModel
from ..models.entities.Contactos import Contacto

main = Blueprint('contacto_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_contactos():
    try:
        contactos = ContactoModel.get_all_contactos()
        if contactos:
            return jsonify(contactos), 200
        else:
            return jsonify({"message": "No se encontraron contactos"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/<id>', methods=['GET'])
def get_contacto_by_id(id):
    try:
        contacto = ContactoModel.get_contacto_by_id(id)
        if contacto:
            return jsonify(contacto), 200
        else:
            return jsonify({"error": "Contacto no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_contacto():
    try:
        data = request.get_json()
        required_fields = ['nombre', 'apellido', 'idcategoria', 'idempresa', 'fecha_nacimiento']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        contacto_id = str(uuid.uuid4())
        contacto = Contacto(
            idcontacto=contacto_id,
            nombre=data['nombre'],
            apellido=data['apellido'],
            idcategoria=data['idcategoria'],
            idempresa=data['idempresa'],
            fecha_nacimiento=data['fecha_nacimiento']
        )
        ContactoModel.add_contacto(contacto)
        return jsonify({"message": "Contacto agregado exitosamente", "id": contacto_id}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/update/<id>', methods=['PUT'])
def update_contacto(id):
    try:
        data = request.get_json()
        existing_contacto = ContactoModel.get_contacto_by_id(id)
        if not existing_contacto:
            return jsonify({"error": "Contacto no encontrado"}), 404

        required_fields = ['nombre', 'apellido', 'idcategoria', 'idempresa', 'fecha_nacimiento']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        contacto = Contacto(
            idcontacto=id,
            nombre=data['nombre'],
            apellido=data['apellido'],
            idcategoria=data['idcategoria'],
            idempresa=data['idempresa'],
            fecha_nacimiento=data['fecha_nacimiento']
        )

        affected_rows = ContactoModel.update_contacto(contacto)
        if affected_rows == 1:
            return jsonify({"message": "Contacto actualizado correctamente"}), 200
        else:
            return jsonify({"error": "No se pudo actualizar el contacto"}), 500
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/delete/<id>', methods=['DELETE'])
def delete_contacto(id):
    try:
        contacto = Contacto(idcontacto=id, nombre="", apellido="", idcategoria="", idempresa="", fecha_nacimiento="01/01/2000")
        affected_rows = ContactoModel.delete_contacto(contacto)
        if affected_rows == 1:
            return jsonify({"message": f"Contacto con ID {id} eliminado"}), 200
        else:
            return jsonify({"error": "Contacto no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
