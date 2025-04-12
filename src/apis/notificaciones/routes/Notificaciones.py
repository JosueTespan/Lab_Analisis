from flask import Blueprint, jsonify, request
import uuid
from datetime import datetime, date


from ..models.entities.Notificaciones import Notificacion
from ..models.NotificacionesModels import NotificacionModel
from ...telefonos.models.TelefonosModels import TelefonoModel
from ..services.servicesTwilio import send_whatsapp_message
from ..services.consulta_notificaciones import get_notification_data

main = Blueprint('notificaciones_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_notificaciones():
    try:
        notificaciones = NotificacionModel.get_all_notificaciones()
        return jsonify(notificaciones), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@main.route('/<id>', methods=['GET'])
def get_notificacion_by_id(id):
    try:
        notificacion = NotificacionModel.get_notificacion_by_id(id)
        if notificacion:
            return jsonify(notificacion), 200
        else:
            return jsonify({"error": "Notificación no encontrada"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_notification():
    try:
        data = request.get_json()
        required_fields = ['idcontacto', 'fecha_envio', 'estado']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({
                "error": "Faltan campos obligatorios: " + ", ".join(missing_fields)
            }), 400

        idcontacto = data.get('idcontacto')
        fecha_envio_str = data.get('fecha_envio')
        estado = data.get('estado')

        try:
            fecha_envio = datetime.strptime(fecha_envio_str, "%Y/%m/%d").date()
        except Exception:
            return jsonify({
                "error": "Formato de fecha_envio inválido, se requiere YYYY/MM/DD"
            }), 400

        notificacion_id = str(uuid.uuid4())
        notificacion = Notificacion(
            id=notificacion_id,
            idcontacto=idcontacto,
            fecha_envio=fecha_envio,
            estado=estado
        )

        affected_rows = NotificacionModel.add_notification(notificacion)
        if affected_rows != 1:
            return jsonify({"error": "No se pudo agregar la notificación"}), 500

        contacto_data = get_notification_data(idcontacto)
        if contacto_data:
            contacto_info = contacto_data[0]
            fecha_nac = contacto_info.get('fecha_nacimiento')

            if isinstance(fecha_nac, (datetime, date)):
                fecha_nac_str = fecha_nac.strftime('%d/%m/%Y')
            else:
                fecha_nac_str = str(fecha_nac) if fecha_nac else 'N/A'

            message_body = (
                f"Notificación para el contacto:\n"
                f"Nombre: {contacto_info.get('nombre', 'N/A')} {contacto_info.get('apellido', '')}\n"
                f"ID Categoría: {contacto_info.get('idcategoria', 'N/A')}\n"
                f"ID Empresa: {contacto_info.get('idempresa', 'N/A')}\n"
                f"Fecha de Nacimiento: {fecha_nac_str}\n"
                f"Fecha de envío: {fecha_envio_str}\n"
                f"Estado: {estado}"
            )
        else:
            message_body = "No se encontraron datos del contacto para esta notificación."

        telefonos = TelefonoModel.get_all_telefonos()
        if not telefonos:
            return jsonify({"error": "No se encontraron destinatarios registrados"}), 404

        send_results = {}
        for tel in telefonos:
            numero = str(tel.get("numero_telefono", "")).strip()
            if not numero:
                send_results["Número no definido"] = {
                    "status": "Error",
                    "error": "Número de teléfono vacío"
                }
                continue

            if not numero.startswith('+'):
                phone_number = "+503" + numero
            else:
                phone_number = numero

            try:
                sid = send_whatsapp_message(phone_number, message_body)
                send_results[phone_number] = {
                    "status": "Enviado",
                    "sid": sid
                }
            except Exception as e:
                send_results[phone_number] = {
                    "status": "Error",
                    "error": str(e)
                }

        return jsonify({
            "id_notificacion": notificacion.id,
            "message": "Notificación agregada y mensajes enviados",
            "send_results": send_results
        }), 200

    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
