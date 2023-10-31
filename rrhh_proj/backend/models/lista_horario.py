from models.horario import Horario
from models.lugar_trabajo import LugarTrabajo
import json

class ListaHorario():
    
    """This class integrates LugarTrabajo and Horario in order to handle them as a collection in which the key is a single LugarTrabajo and the  value
    could be list of Horarios with differents days and its time"""

    #region construct
    def __init__(self):
        self.lista_horario={}
    #endregion

    #region methods
    """
    We accept an instance of LugarTrabajo and a list of Horarios. 
    We then use the extend method to add the Horarios to the existing list of Horarios associated with the LugarTrabajo.
    """
    def add_horario_lugar_trabajo(self,lugar_trabajo,horarios):
        if lugar_trabajo not in self.lista_horario:
            self.lista_horario[lugar_trabajo]=[]
        if isinstance(horarios, list):
            self.lista_horario[lugar_trabajo].extend(horarios)
        else:
            self.lista_horario[lugar_trabajo].append(horarios)

    """
    It removes a specific Horario from a LugarTrabajo and also removes LugarTrabajo if it no longer has associated Horarios.
    """
    def remove_horario_lugar_trabajo(self, lugar_trabajo,horario):
        if lugar_trabajo in self.lista_horario and horario  in self._listaHorario[lugar_trabajo]:
            self.lista_horario[lugar_trabajo].remove(horario)
            if not self.lista_horario[lugar_trabajo]:
                del self.lista_horario[lugar_trabajo]
    
    #show_horarios_por_lugar
    """
    The key in the dictionary horarios_dict will be the combination of Empresa and Sucursal of LugarTrabajo. 
    This will allow it to group Horarios under the unique combinations of Empresa and Sucursal instead of just the company name.
    """
    def show_data(self):
        horarios_dict={}
        for lugar,horarios in self.lista_horario.items():
            lugar_combination=lugar.get_empresa_sucursal_combination()
            #horarios_dict[lugar_combination]= [horario.show_data() for horario in horarios]
            
            horarios_info = []
            #Adding a numbered range/availability subtitle for each timetable
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
    #endregion


   

    
