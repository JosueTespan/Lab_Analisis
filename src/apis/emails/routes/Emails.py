from flask import Blueprint, jsonify, request
import uuid
from ..models.EmailsModels import EmailModel
from ..models.entities.Emails import Email

main = Blueprint('email_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_emails():
    try:
        emails = EmailModel.get_all_emails()
        if emails:
            return jsonify(emails), 200
        else:
            return jsonify({"message": "No se encontraron emails"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/<id>', methods=['GET'])
def get_email_by_id(id):
    try:
        email = EmailModel.get_email_by_id(id)
        if email:
            return jsonify(email), 200
        else:
            return jsonify({"error": "Email no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_email():
    try:
        data = request.get_json()
        required_fields = ['idcontacto', 'tipo', 'email']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400
        
        email_id = str(uuid.uuid4())
        email = Email(
            idemail=email_id,
            idcontacto=data['idcontacto'],
            tipo=data['tipo'],
            email=data['email']
        )
        EmailModel.add_email(email)
        return jsonify({"message": "Email agregado exitosamente", "id": email_id}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/update/<id>', methods=['PUT'])
def update_email(id):
    try:
        data = request.get_json()
        existing_email = EmailModel.get_email_by_id(id)
        if not existing_email:
            return jsonify({"error": "Email no encontrado"}), 404

        required_fields = ['idcontacto', 'tipo', 'email']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        email = Email(
            idemail=id,
            idcontacto=data['idcontacto'],
            tipo=data['tipo'],
            email=data['email']
        )

        affected_rows = EmailModel.update_email(email)
        if affected_rows == 1:
            return jsonify({"message": "Email actualizado correctamente"}), 200
        else:
            return jsonify({"error": "No se pudo actualizar el email"}), 500
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/delete/<id>', methods=['DELETE'])
def delete_email(id):
    try:
        email = Email(idemail=id, idcontacto="", tipo="", email="")
        affected_rows = EmailModel.delete_email(email)
        if affected_rows == 1:
            return jsonify({"message": f"Email con ID {id} eliminado"}), 200
        else:
            return jsonify({"error": "Email no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
