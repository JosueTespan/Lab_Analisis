from flask import Blueprint, jsonify, request
import uuid
from ..models.TelefonosModels import TelefonoModel
from ..models.entities.Telefonos import Telefono

main = Blueprint('telefono_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_telefonos():
    try:
        telefonos = TelefonoModel.get_all_telefonos()
        if telefonos:
            return jsonify(telefonos), 200
        else:
            return jsonify({"message": "No se encontraron teléfonos"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/<id>', methods=['GET'])
def get_telefono_by_id(id):
    try:
        telefono = TelefonoModel.get_telefono_by_id(id)
        if telefono:
            return jsonify(telefono), 200
        else:
            return jsonify({"error": "Teléfono no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_telefono():
    try:
        data = request.get_json()
        required_fields = ['idcontacto', 'tipo', 'numero']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400
        
        telefono_id = str(uuid.uuid4())
        telefono = Telefono(
            idtelefono=telefono_id,
            idcontacto=data['idcontacto'],
            tipo=data['tipo'],
            numero=data['numero']
        )
        TelefonoModel.add_telefono(telefono)
        return jsonify({"message": "Teléfono agregado exitosamente", "id": telefono_id}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/update/<id>', methods=['PUT'])
def update_telefono(id):
    try:
        data = request.get_json()
        existing_telefono = TelefonoModel.get_telefono_by_id(id)
        if not existing_telefono:
            return jsonify({"error": "Teléfono no encontrado"}), 404

        required_fields = ['idcontacto', 'tipo', 'numero']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        telefono = Telefono(
            idtelefono=id,
            idcontacto=data['idcontacto'],
            tipo=data['tipo'],
            numero=data['numero']
        )

        affected_rows = TelefonoModel.update_telefono(telefono)
        if affected_rows == 1:
            return jsonify({"message": "Teléfono actualizado correctamente"}), 200
        else:
            return jsonify({"error": "No se pudo actualizar el teléfono"}), 500
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/delete/<id>', methods=['DELETE'])
def delete_telefono(id):
    try:
        telefono = Telefono(idtelefono=id, idcontacto="", tipo="", numero="")
        affected_rows = TelefonoModel.delete_telefono(telefono)
        if affected_rows == 1:
            return jsonify({"message": f"Teléfono con ID {id} eliminado"}), 200
        else:
            return jsonify({"error": "Teléfono no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
