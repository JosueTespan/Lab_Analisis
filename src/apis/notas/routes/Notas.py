from flask import Blueprint, jsonify, request
import uuid
from ..models.NotasModels import NotaModel
from ..models.entities.Notas import Nota

main = Blueprint('nota_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_notas():
    try:
        notas = NotaModel.get_all_notas()
        if notas:
            return jsonify(notas), 200
        else:
            return jsonify({"message": "No se encontraron notas"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/<id>', methods=['GET'])
def get_nota_by_id(id):
    try:
        nota = NotaModel.get_nota_by_id(id)
        if nota:
            return jsonify(nota), 200
        else:
            return jsonify({"error": "Nota no encontrada"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_nota():
    try:
        data = request.get_json()
        required_fields = ['idcontacto', 'nota', 'fecha']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        nota_id = str(uuid.uuid4())
        nota = Nota(
            idnota=nota_id,
            idcontacto=data['idcontacto'],
            nota=data['nota'],
            fecha=data['fecha']
        )
        NotaModel.add_nota(nota)
        return jsonify({"message": "Nota agregada exitosamente", "id": nota_id}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/update/<id>', methods=['PUT'])
def update_nota(id):
    try:
        data = request.get_json()
        existing_nota = NotaModel.get_nota_by_id(id)
        if not existing_nota:
            return jsonify({"error": "Nota no encontrada"}), 404

        required_fields = ['idcontacto', 'nota', 'fecha']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        nota = Nota(
            idnota=id,
            idcontacto=data['idcontacto'],
            nota=data['nota'],
            fecha=data['fecha']
        )

        affected_rows = NotaModel.update_nota(nota)
        if affected_rows == 1:
            return jsonify({"message": "Nota actualizada correctamente"}), 200
        else:
            return jsonify({"error": "No se pudo actualizar la nota"}), 500
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/delete/<id>', methods=['DELETE'])
def delete_nota(id):
    try:
        nota = Nota(idnota=id, idcontacto="", nota="", fecha="2000-01-01")
        affected_rows = NotaModel.delete_nota(nota)
        if affected_rows == 1:
            return jsonify({"message": f"Nota con ID {id} eliminada"}), 200
        else:
            return jsonify({"error": "Nota no encontrada"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
