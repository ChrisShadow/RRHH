from models.horario import Horario
from models.lugar_trabajo import LugarTrabajo
import json


class ListaHorario():

    """This class integrates LugarTrabajo and Horario in order to handle them as a collection in which the key is a single LugarTrabajo and the  value
    could be list of Horarios with differents days and its time"""

    # region construct
    def __init__(self):
        self.lista_horario = {}
    # endregion

    # region methods
    """
    We accept an instance of LugarTrabajo and a list of Horarios. 
    We then use the extend method to add the Horarios to the existing list of Horarios associated with the LugarTrabajo.
    """

    def add_horario_lugar_trabajo(self, lugar_trabajo, horarios):
        if lugar_trabajo not in self.lista_horario:
            self.lista_horario[lugar_trabajo] = []
        if isinstance(horarios, list):
            self.lista_horario[lugar_trabajo].extend(horarios)
        else:
            self.lista_horario[lugar_trabajo].append(horarios)

    def update_horario_lugar_trabajo(self, lugar_trabajo, new_horarios):
        if lugar_trabajo in self.lista_horario:
            # Replacing the new ones
            self.lista_horario[lugar_trabajo] = new_horarios
            print(
                f"Horario actualizado a {lugar_trabajo.get_empresa_sucursal_combination()}")
        else:
            print(
                f"No se encontró el lugar de trabajo o el horario antiguo para {lugar_trabajo}")

    """
    It removes a specific Horario from a LugarTrabajo and also removes LugarTrabajo if it no longer has associated Horarios.
    """

    def remove_horarios_lugar_trabajo(self, lugar_trabajo, *horarios):
        if lugar_trabajo in self.lista_horario:
            # List of horarios added to lugar_trabajo
            horarios_lugar = self.lista_horario[lugar_trabajo]

            # Deleting those horarios
            for horario in horarios:
                if horario in horarios_lugar:
                    horarios_lugar.remove(horario)

            # In case of zero horarios, then the lugar_trabajo
            """if not horarios_lugar:
                del self.lista_horario[lugar_trabajo]"""
        else:
            print(f"No se encontró el lugar de trabajo {lugar_trabajo}")

    # show_horarios_por_lugar
    """
    The key in the dictionary horarios_dict will be the combination of Empresa and Sucursal of LugarTrabajo. 
    This will allow it to group Horarios under the unique combinations of Empresa and Sucursal instead of just the company name.
    """

    def show_data(self):
        horarios_dict = {}
        for lugar, horarios in self.lista_horario.items():
            lugar_combination = lugar.get_empresa_sucursal_combination()
            # horarios_dict[lugar_combination]= [horario.show_data() for horario in horarios]

            horarios_info = []
            # Adding a numbered range/availability subtitle for each timetable
            for i, horario in enumerate(horarios, start=1):
                horario_data = {
                    f"Rango {i}": {
                        "Dias:": ", ".join(horario.get_dias()),
                        "Desde:": horario.get_hora_inicio(),
                        "Hasta:": horario.get_hora_fin()
                    }
                }
                horarios_info.append(horario_data)

            horarios_dict[lugar_combination] = horarios_info

        return json.dumps(horarios_dict)
    # endregion
