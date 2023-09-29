from actividades import Actividades
import json


class ListaActividades():

    #region constructor
    def __init__(self):
        self.lista_actividad={}
    #endregion

    #region methods
    def add_actividad(self, name,level):
        actividad=Actividades(name,level)
        self.lista_actividad[name]=actividad

    def update_actividad(self, name, level):
        if name in self.lista_actividad:
            actividad=self.lista_actividad[name]
            actividad.set_nivel(level)

    def remove_actividad(self,name):
        if name in self.lista_actividad:
            del self.lista_actividad[name]

    def show_data(self):
        act_dict={}
        for actividad in self.lista_actividad:
            act_dict[actividad.get_nombre()]=actividad.get_nivel()
        return json.dumps(act_dict)
    #endregion
