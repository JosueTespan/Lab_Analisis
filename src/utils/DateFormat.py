import datetime

class DateFormat():
    @classmethod
    def convert_date(cls, date):
        # Si el argumento ya es un objeto datetime.date o datetime.datetime
        if isinstance(date, (datetime.date, datetime.datetime)):
            date_obj = date
        else:
            # Parsear la cadena de fecha (formato esperado: 'YYYY-MM-DD')
            date_obj = datetime.datetime.strptime(date, '%d/%m/%Y')
        
        # Retornar en el nuevo formato
        return date_obj.strftime('%d/%m/%Y')
