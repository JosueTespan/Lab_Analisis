from flask import Blueprint, jsonify, request
import uuid
from ..models.HistorialModels import HistorialModel
from ..models.entities.Historial import Historial
from datetime import datetime

main = Blueprint('historial_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_historiales():
    try:
        historiales = HistorialModel.get_all_historiales()
        if historiales:
            return jsonify(historiales), 200
        else:
            return jsonify({"message": "No se encontraron historiales"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@main.route('/<id>', methods=['GET'])
def get_historial_by_id(id):
    try:
        historial = HistorialModel.get_historial_by_id(id)
        if historial:
            return jsonify(historial), 200
        else:
            return jsonify({"error": "Historial no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_historial():
    try:
        data = request.get_json()
        required_fields = ['idcontacto', 'descripcion', 'fecha']
        missing_fields = [f for f in required_fields if f not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        historial_id = str(uuid.uuid4())

        # Validación de fecha
        try:
            fecha = datetime.strptime(data['fecha'], "%Y-%m-%d").date()
        except ValueError:
            return jsonify({"error": "Formato de fecha inválido. Use YYYY-MM-DD"}), 400

        historial = Historial(
            idhistorial=historial_id,
            idcontacto=data['idcontacto'],
            descripcion=data['descripcion'],
            fecha=fecha
        )
        HistorialModel.add_historial(historial)
        return jsonify({"message": "Historial agregado exitosamente", "id": historial_id}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_historial(id):
    try:
        data = request.get_json()
        historial_existente = HistorialModel.get_historial_by_id(id)
        if not historial_existente:
            return jsonify({"error": "Historial no encontrado"}), 404

        required_fields = ['idcontacto', 'descripcion', 'fecha']
        missing_fields = [f for f in required_fields if f not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        try:
            fecha = datetime.strptime(data['fecha'], "%Y-%m-%d").date()
        except ValueError:
            return jsonify({"error": "Formato de fecha inválido. Use YYYY-MM-DD"}), 400

        historial = Historial(
            idhistorial=id,
            idcontacto=data['idcontacto'],
            descripcion=data['descripcion'],
            fecha=fecha
        )
        rows = HistorialModel.update_historial(historial)
        if rows == 1:
            return jsonify({"message": "Historial actualizado correctamente"}), 200
        else:
            return jsonify({"error": "No se pudo actualizar el historial"}), 500
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_historial(id):
    try:
        historial = Historial(idhistorial=id, idcontacto="", descripcion="", fecha="2000-01-01")
        rows = HistorialModel.delete_historial(historial)
        if rows == 1:
            return jsonify({"message": f"Historial con ID {id} eliminado"}), 200
        else:
            return jsonify({"error": "Historial no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
