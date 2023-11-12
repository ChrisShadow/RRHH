from models.actividades import Actividades
import json


class ListaActividades():

    #region constructor
    def __init__(self):
        self.lista_actividad={}
    #endregion

    #region methods
    def add_actividad(self,*actividades):
        for actividad in actividades:
            self.lista_actividad[actividad.get_nombre()]=actividad

    def update_actividad(self, name, level):
        if name in self.lista_actividad:
           self.lista_actividad[name].set_nivel(level)

    def remove_actividades(self, *actividades):
        for actividad in actividades:
            for name, instance in list(self.lista_actividad.items()):
                if instance == actividad:
                    del self.lista_actividad[name]
                    break
    
    def show_data(self):
        act_dict={}
        for name,actividad in self.lista_actividad.items():
            act_dict[name]=actividad.get_nivel()
        return json.dumps(act_dict)

    #endregion