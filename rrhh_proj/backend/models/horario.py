import json


class Horario():

    # region constructor
    def __init__(self, dia, hora_inicio, hora_fin):
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
    # endregion

    # region getter
    def get_dia(self):
        return self.dia

    def get_hora_inicio(self):
        return self.hora_inicio

    def get_hora_fin(self):
        return self.hora_fin
    # endregion

    # region setter
    def set_dia(self, new_day):
        self.dia = new_day

    def set_hora_inicio(self, new_starting_hour):
        self.hora_inicio = new_starting_hour

    def set_hora_fin(self, new_leaving_hour):
        self.hora_fin = new_leaving_hour
    # endregion

    # region methods
    @classmethod
    def crate_from_string(cls, data_string):
        dia, hora_inicio, hora_fin = data_string.split(
            ",")
        return cls(dia.strip(), hora_inicio.strip(), hora_fin.strip())

    @classmethod
    def show_data(cls, horario):
        response = {
            "Día: ": horario.get_dia(),
            "Desde: ": horario.get_hora_inicio(),
            "Hasta: ": horario.get_hora_fin()
        }
        json_response = json.dumps(response)
        return json_response
    # endregion