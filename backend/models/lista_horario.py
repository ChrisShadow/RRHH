from models.horario import Horario
from models.lugar_trabajo import LugarTrabajo
import json

class ListaHorario():
    
    """This class integrates LugarTrabajo and Horario in order to handle them as a collection in which the key is a single LugarTrabajo and the  value
    could be list of Horarios with differents days and its time"""

    #region construct
    def __init__(self):
        self._listaHorario={}
    #endregion

    #region getter
    def get_lista_horario(self):
        return self._listaHorario
    #endregion

    #region setter
    def set_lista_horario(self, new_list):
        self._listaHorario=new_list
    #endregion

    #region methods
    """
    We accept an instance of LugarTrabajo and a list of Horarios. 
    We then use the extend method to add the Horarios to the existing list of Horarios associated with the LugarTrabajo.
    """
    @classmethod
    def add_horario_lugar_trabajo(self,lugar_trabajo,horarios):
        if lugar_trabajo not in self._listaHorario:
            self._listaHorario[lugar_trabajo]=[]
        self._listaHorario[lugar_trabajo].extend(horarios)

    """
    A specific Horario is added to an existing LugarTrabajo in the Horario list without deleting existing Horarios. 
    Useful for expanding the list of Horarios  associated with a LugarTrabajo.
    """
    def add_horario_to_lugar_trabajo(self,lugar_trabajo,horario):
        if lugar_trabajo in self._listaHorario:
            self._listaHorario[lugar_trabajo].append(horario)

    """"
    It removes a specific Horario from a LugarTrabajo and also removes LugarTrabajo if it no longer has associated Horarios.
    """
    def remove_horario_lugar_trabajo(self, lugar_trabajo,horario):
        if lugar_trabajo in self._listaHorario and horario  in self._listaHorario[lugar_trabajo]:
            self._listaHorario[lugar_trabajo].remove(horario)
            if not self._listaHorario[lugar_trabajo]:
                del self._listaHorario[lugar_trabajo]
    
    #show_horarios_por_lugar
    """
    The key in the dictionary horarios_dict will be the combination of Empresa and Sucursal of LugarTrabajo. 
    This will allow it to group Horarios under the unique combinations of Empresa and Sucursal instead of just the company name.
    """
    @classmethod
    def show_data(self):
        horarios_dict={}
        for lugar,horarios in self._listaHorario.items():
            lugar_combination=lugar.get_empresa_sucursal_combination()
            horarios_dict[lugar_combination]= [horario.show_data() for horario in horarios]
        return json.dumps(horarios_dict)
    #endregion


   

    
