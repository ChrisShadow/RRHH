import json


class Actividades():
    # region constructor:
    """a Python class constructor. It takes two parameters, 
    "nombre" and "nivel", and initializes the instance variables with the same names."""

    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel
    # endregion

    # region getter
    """It defines two methods, get_nombre and get_nivel, 
    which return the value of the instance variables nombre and nivel respectively."""

    def get_nombre(self):
        return self.nombre

    def get_nivel(self):
        return self.nivel
    # endregion

    # region setter
    """It defines a class method to set the name and level of an activity. 
    It also includes a validation check to ensure that the level is one 
    of the valid options: 'Alto', 'Medio', or 'Bajo'. 
    If the provided level is not valid, it sets the level to 'Medio(Default)'."""

    def set_nombre(self, new_name):
        self.nombre = new_name

    def set_nivel(self, new_level):
        valid_options = ['Alto', 'Medio', 'Bajo']
        if new_level in valid_options:
            self.nivel = new_level
        else:
            # raise ValueError("Prioridad no válida. Debe ser 'Alto', 'Medio' o 'Bajo'.")
            print(("Prioridad no válida. Debe ser 'Alto', 'Medio' o 'Bajo'."))
            self.nivel = 'Medio(Default)'
    # endregion

    # region methods
    """This defines a class method "create_from_string" that takes a string as input,
    splits it into two parts, and creates an instance of the class 
    with the extracted values. If the second part of the string 
    is not a valid priority level, it sets the priority level to "Medio(Default)"."""
    @classmethod
    def create_from_string(cls, data_string):
        nombre, nivel = map(str.strip, data_string.lstrip().split(":"))

        if nivel.lstrip() not in ['Alto', 'Medio', 'Bajo']:
            # raise ValueError("Prioridad no válida. Debe ser 'Alto', 'Medio' o 'Bajo'.")
            print("Prioridad no válida. Debe ser 'Alto', 'Medio' o 'Bajo'.")
            nivel = 'Medio(Default)'
        return cls(nombre.strip(), nivel.strip())

    """This defines a class method named "show_data" which takes an object 
    of "actividades" class as input and returns a JSON response containing 
    the name and priority level of the activity"""
    @classmethod
    def show_data(cls, actividades):
        response = {
            "Nombre de la responsabilidad: ": actividades.get_nombre(),
            "Prioridad del cargo": actividades.get_nivel()
        }
        json_response = json.dumps(response)
        return json_response
    # endregion
