from flask import Blueprint, jsonify, request
import uuid
from ..models.CategoriaModels import CategoriaModel
from ..models.entities.Categoria import Categoria

main = Blueprint('categoria_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_categorias():
    try:
        categorias = CategoriaModel.get_all_categoria()
        if categorias:
            return jsonify(categorias), 200
        else:
            return jsonify({"message": "no se encontro la categoria"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/<id>', methods=['GET'])
def get_categoria_by_id(id):
    try:
        categoria = CategoriaModel.get_categoria_by_id(id)
        if categoria:
            return jsonify(categoria)
        else:
            return jsonify({"Error": "Categoria no encontrada"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_categoria():
    try:
        data = request.get_json()
        required_fields = ['nombre', 'descripcion']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400 
        
        categoria_id = str(uuid.uuid4())
        categoria = Categoria(
            IdCategoria=categoria_id,
            nombre=data['nombre'],
            descripcion=data['descripcion']
        )
        CategoriaModel.add_categoria(categoria)
        return jsonify({"message": "Categoría agregada exitosamente", "id": categoria_id}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/update/<id>', methods=['PUT'])
def update_categoria(id):
    try:
        data = request.get_json()
        existing_categoria = CategoriaModel.get_categoria_by_id(id)
        if not existing_categoria:
            return jsonify({"error": "Categoría no encontrada"}), 404

        required_fields = ['nombre', 'descripcion']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        categoria = Categoria(
            IdCategoria=id,
            nombre=data['nombre'],
            descripcion=data['descripcion']
        )

        affected_rows = CategoriaModel.update_categoria(categoria)
        if affected_rows == 1:
            return jsonify({"message": "Categoría actualizada correctamente"}), 200
        else:
            return jsonify({"error": "No se pudo actualizar la categoría"}), 500
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/delete/<id>', methods=['DELETE'])
def delete_categoria(id):
    try:
        categoria = Categoria(IdCategoria=id, nombre="", descripcion="")
        affected_rows = CategoriaModel.delete_categoria(categoria)
        if affected_rows == 1:
            return jsonify({"message": f"Categoría con ID {id} eliminada"}), 200
        else:
            return jsonify({"error": "Categoría no encontrada"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500