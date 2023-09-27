import json

class Actividades():
    #region constructor
    def __init__(self,nombre, nivel):
        self.nombre=nombre
        self.nivel=nivel
    #endregion

    #region getter
    def get_nombre(self):
        return self.nombre
    
    def get_nivel(self):
        return self.nivel
    #endregion

    #region setter
    def set_nombre(self,new_name):
        self.nombre=new_name

    def set_nivel(self, new_level):
        valid_options=['Alto', 'Medio', 'Bajo']
        if new_level in valid_options:
            self.nivel=new_level
        else:
            print("Prioridad no válida. Debe ser 'Alto', 'Medio' o 'Bajo'.")
    #endregion

    #region methods

    """
    This function is required because of the values for each created instance of the class. 
    It does create an object from a data string
    """
    @classmethod
    def create_from_string(cls,data_string):
        nombre, nivel=data_string.split(":")
        return cls(nombre.strip(),nivel.strip())

    """ and then the show_data method can be used as a class method, too. It returns a string 
    representation of the attributes of the Actividades passed as an argument."""
    @classmethod
    def show_data(cls, actividades):
        response={
            "Nombre de la responsabilidad: ": actividades.get_nombre(),
            "Prioridad del cargo": actividades.get_nivel()
        }
        json_response=json.dumps(response)
        return json_response
    #endregion