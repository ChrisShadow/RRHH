from models.actividades import Actividades
import json


class ListaActividades():

    # region constructor
    def __init__(self):
        self.lista_actividad = {}
    # endregion

    # region methods
    def add_actividad(self, *actividades):
        for actividad in actividades:
            self.lista_actividad[actividad.get_nombre()] = actividad

    def update_actividad(self, old_name, new_name, level):
        if old_name in self.lista_actividad:
            # Getting the old instance of Actividad
            actividad = self.lista_actividad[old_name]

            # Updating de new values
            actividad.set_nombre(new_name)
            actividad.set_nivel(level)

            # If the name has changed, setting the key in the dict
            if old_name != new_name:
                del self.lista_actividad[old_name]
                self.lista_actividad[new_name] = actividad
        else:
            print(f"No se encontró la actividad con el nombre {old_name}")

    def remove_actividades(self, *actividades):
        for actividad in actividades:
            # Before deleting
            if actividad in self.lista_actividad.values():
                for name, instance in list(self.lista_actividad.items()):
                    if instance == actividad:
                        del self.lista_actividad[name]
                        break
            else:
                print(f"No se encontró la actividad {actividad}")

    def show_data(self):
        act_dict = {}
        for name, actividad in self.lista_actividad.items():
            act_dict[name] = actividad.get_nivel()
        return json.dumps(act_dict)

    # endregion
