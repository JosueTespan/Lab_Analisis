from flask import Blueprint, jsonify, request
import uuid
from ..models.DireccionesModels import DireccionModel
from ..models.entities.Direcciones import Direccion

main = Blueprint('direccion_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_direcciones():
    try:
        direcciones = DireccionModel.get_all_direcciones()
        if direcciones:
            return jsonify(direcciones), 200
        else:
            return jsonify({"message": "No se encontraron direcciones"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/<id>', methods=['GET'])
def get_direccion_by_id(id):
    try:
        direccion = DireccionModel.get_direccion_by_id(id)
        if direccion:
            return jsonify(direccion)
        else:
            return jsonify({"error": "Dirección no encontrada"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_direccion():
    try:
        data = request.get_json()
        required_fields = ['idcontacto', 'direccion', 'ciudad', 'estado', 'pais', 'codigo_postal']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        direccion_id = str(uuid.uuid4())
        direccion = Direccion(
            iddireccion=direccion_id,
            idcontacto=data['idcontacto'],
            direccion=data['direccion'],
            ciudad=data['ciudad'],
            estado=data['estado'],
            pais=data['pais'],
            codigo_postal=data['codigo_postal']
        )
        DireccionModel.add_direccion(direccion)
        return jsonify({"message": "Dirección agregada exitosamente", "id": direccion_id}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/update/<id>', methods=['PUT'])
def update_direccion(id):
    try:
        data = request.get_json()
        existing_direccion = DireccionModel.get_direccion_by_id(id)
        if not existing_direccion:
            return jsonify({"error": "Dirección no encontrada"}), 404

        required_fields = ['idcontacto', 'direccion', 'ciudad', 'estado', 'pais', 'codigo_postal']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        direccion = Direccion(
            iddireccion=id,
            idcontacto=data['idcontacto'],
            direccion=data['direccion'],
            ciudad=data['ciudad'],
            estado=data['estado'],
            pais=data['pais'],
            codigo_postal=data['codigo_postal']
        )

        affected_rows = DireccionModel.update_direccion(direccion)
        if affected_rows == 1:
            return jsonify({"message": "Dirección actualizada correctamente"}), 200
        else:
            return jsonify({"error": "No se pudo actualizar la dirección"}), 500
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/delete/<id>', methods=['DELETE'])
def delete_direccion(id):
    try:
        direccion = Direccion(
            iddireccion=id,
            idcontacto="",
            direccion="",
            ciudad="",
            estado="",
            pais="",
            codigo_postal=""
        )
        affected_rows = DireccionModel.delete_direccion(direccion)
        if affected_rows == 1:
            return jsonify({"message": f"Dirección con ID {id} eliminada"}), 200
        else:
            return jsonify({"error": "Dirección no encontrada"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
