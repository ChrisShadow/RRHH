from models.actividades import Actividades
import json


class ListaActividades():

    """This class integrates Actividades in order to handle them as a collection 
    in which the key is the name of it and the  value is the level  of the activity"""

    # region constructor
    """An attribute called 'lista_actividad' which is initialized as an empty dictionary."""

    def __init__(self):
        self.lista_actividad = {}
    # endregion

    # region methods
    """ It defines a function  add_actividad  which takes a variable number 
    of activity objects and adds them to a list called  lista_actividad . 
    Each activity is stored in the list with its name as the key. 
    The function does not return anything."""

    def add_actividad(self, *actividades):
        for actividad in actividades:
            self.lista_actividad[actividad.get_nombre()] = actividad

    """It defines a function  update_actividad  that updates the name and level
    of an activity in a list. It checks if the old_name exists in the list, 
    retrieves the old instance of the activity, updates the new values, and if
    the name has changed, updates the key in the dictionary. If the old_name 
    is not found, it prints a message indicating that the activity was not found."""

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

    """It defines a method called "remove_actividades" which takes in variable 
    number of "actividades" as arguments. It iterates through each "actividad" 
    and checks if it exists in a dictionary called "lista_actividad". If found,
    it deletes the corresponding entry from the dictionary. If not found, 
    it prints a message indicating that the activity was not found."""

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

    """It defines a method called "show_data" that takes a self parameter. It 
    creates an empty dictionary called "act_dict" and iterates over the items
    in the "lista_actividad" dictionary. For each item, it retrieves the 
    "nivel" attribute of the "actividad" object and stores it in the "act_dict" 
    dictionary with the corresponding name. Finally, it returns the JSON 
    representation of the "act_dict" dictionary."""

    def show_data(self):
        act_dict = {}
        for name, actividad in self.lista_actividad.items():
            act_dict[name] = actividad.get_nivel()
        return json.dumps(act_dict)

    # endregion
