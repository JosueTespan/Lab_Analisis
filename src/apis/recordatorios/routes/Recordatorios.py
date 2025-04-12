from flask import Blueprint, jsonify, request
import uuid
from ..models.RecordatoriosModels import RecordatoriosModels
from ..models.entities.Recordatorios import Recordatorios

main = Blueprint('recordatorio_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_recordatorios():
    try:
        recordatorios = RecordatoriosModels.get_all_recordatorios()
        if recordatorios:
            return jsonify(recordatorios), 200
        else:
            return jsonify({"message": "No se encontraron recordatorios"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/<id>', methods=['GET'])
def get_recordatorio_by_id(id):
    try:
        recordatorio = RecordatoriosModels.get_recordatorio_by_id(id)
        if recordatorio:
            return jsonify(recordatorio), 200
        else:
            return jsonify({"error": "Recordatorio no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_recordatorio():
    try:
        data = request.get_json()
        required_fields = ['idcontacto', 'descripcion', 'fecha_recordatorio', 'completado']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        recordatorio_id = str(uuid.uuid4())
        recordatorio = Recordatorios(
            idrecordatorio=recordatorio_id,
            idcontacto=data['idcontacto'],
            descripcion=data['descripcion'],
            fecha_recordatorio=data['fecha_recordatorio'],
            completado=data['completado']
        )
        RecordatoriosModels.add_recordatorio(recordatorio)
        return jsonify({"message": "Recordatorio agregado exitosamente", "id": recordatorio_id}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/update/<id>', methods=['PUT'])
def update_recordatorio(id):
    try:
        data = request.get_json()
        existing_recordatorio = RecordatoriosModels.get_recordatorio_by_id(id)
        if not existing_recordatorio:
            return jsonify({"error": "Recordatorio no encontrado"}), 404

        required_fields = ['idcontacto', 'descripcion', 'fecha_recordatorio', 'completado']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        recordatorio = Recordatorios(
            idrecordatorio=id,
            idcontacto=data['idcontacto'],
            descripcion=data['descripcion'],
            fecha_recordatorio=data['fecha_recordatorio'],
            completado=data['completado']
        )

        affected_rows = RecordatoriosModels.update_recordatorio(recordatorio)
        if affected_rows == 1:
            return jsonify({"message": "Recordatorio actualizado correctamente"}), 200
        else:
            return jsonify({"error": "No se pudo actualizar el recordatorio"}), 500
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/delete/<id>', methods=['DELETE'])
def delete_recordatorio(id):
    try:
        affected_rows = RecordatoriosModels.delete_recordatorio(id)
        if affected_rows == 1:
            return jsonify({"message": f"Recordatorio con ID {id} eliminado"}), 200
        else:
            return jsonify({"error": "Recordatorio no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
