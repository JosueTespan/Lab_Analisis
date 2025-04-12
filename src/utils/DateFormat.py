import datetime

class DateFormat:
    @classmethod
    def convert_date(cls, date_str):
        if isinstance(date_str, (datetime.date, datetime.datetime)):
            return date_str
        try:
            return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            try:
                return datetime.datetime.strptime(date_str, '%d/%m/%Y').date()
            except ValueError:
                raise ValueError(f"Formato de fecha no válido: {date_str}")
