import json


class Horario():

    # region constructor
    def __init__(self, dias, hora_inicio, hora_fin):
        self.dias = dias
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
    # endregion

    # region getter
    def get_dias(self):
        return self.dias

    def get_hora_inicio(self):
        return self.hora_inicio

    def get_hora_fin(self):
        return self.hora_fin
    # endregion

    # region setter
    def set_dias(self, new_days):
        """accepts a list of days and checks if all days entered are valid. 
        If they are all valid, it updates the value of the _days attribute, and if they are not, 
        it generates a ValueError."""
        dias_posibles = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        if all(dia in dias_posibles for dia in new_days):
            self._dias = new_days
        else:
            raise ValueError("Día(s) inválido(s)")

    def set_hora_inicio(self, new_starting_hour):
        self.hora_inicio = new_starting_hour

    def set_hora_fin(self, new_leaving_hour):
        self.hora_fin = new_leaving_hour
    # endregion

    # region methods
    @classmethod
    def create_from_string(cls, data_string):
        dias, hora_inicio, hora_fin = data_string.split(
            ",")
        return cls(dias.strip(), hora_inicio.strip(), hora_fin.strip())

    @classmethod
    def show_data(cls, horario):
        days = horario.get_dias()
        days_combined = ", ".join(days)  # Joining days with a comma and a space
        response = {
            "Días: ": days_combined,
            "Desde: ": horario.get_hora_inicio(),
            "Hasta: ": horario.get_hora_fin()
        }
        json_response = json.dumps(response)
        return json_response
    # endregion
