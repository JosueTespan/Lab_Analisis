from flask import Blueprint, jsonify, request
import uuid
from ..models.EmpresaModels import EmpresaModel
from ..models.entities.Empresa import Empresa

main = Blueprint('empresa_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_empresas():
    try:
        empresas = EmpresaModel.get_all_empresas()
        if empresas:
            return jsonify(empresas), 200
        else:
            return jsonify({"message": "No se encontraron empresas"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/<id>', methods=['GET'])
def get_empresa_by_id(id):
    try:
        empresa = EmpresaModel.get_empresa_by_id(id)
        if empresa:
            return jsonify(empresa)
        else:
            return jsonify({"error": "Empresa no encontrada"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_empresa():
    try:
        data = request.get_json()
        required_fields = ['nombre', 'categoria']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        empresa_id = str(uuid.uuid4())
        empresa = Empresa(
            idempresa=empresa_id,
            nombre=data['nombre'],
            categoria=data['categoria']
        )
        EmpresaModel.add_empresa(empresa)
        return jsonify({"message": "Empresa agregada exitosamente", "id": empresa_id}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/update/<id>', methods=['PUT'])
def update_empresa(id):
    try:
        data = request.get_json()
        existing_empresa = EmpresaModel.get_empresa_by_id(id)
        if not existing_empresa:
            return jsonify({"error": "Empresa no encontrada"}), 404

        required_fields = ['nombre', 'categoria']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        empresa = Empresa(
            idempresa=id,
            nombre=data['nombre'],
            categoria=data['categoria']
        )

        affected_rows = EmpresaModel.update_empresa(empresa)
        if affected_rows == 1:
            return jsonify({"message": "Empresa actualizada correctamente"}), 200
        else:
            return jsonify({"error": "No se pudo actualizar la empresa"}), 500
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/delete/<id>', methods=['DELETE'])
def delete_empresa(id):
    try:
        empresa = Empresa(idempresa=id, nombre="", categoria="")
        affected_rows = EmpresaModel.delete_empresa(empresa)
        if affected_rows == 1:
            return jsonify({"message": f"Empresa con ID {id} eliminada"}), 200
        else:
            return jsonify({"error": "Empresa no encontrada"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
