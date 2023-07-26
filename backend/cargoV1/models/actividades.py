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
        self.nivel=new_level
    #endregion

    #region methods

    """It creates an Actividades object from a data string and uses the show_data() method to display the 
    attributes of the created object. Class methods must have cls as the first parameter, which represents 
    the class itself, so that they can access the class attributes and methods correctly. show_data() as a 
    non-class method, but an instance method as we do not need to access the class attributes. We simply use 
    it to show the instance attributes of the Actividades object."""
    @classmethod
    def crate_from_string(cls,data_string):
        nombre, nivel=data_string.split(":")
        return cls(nombre.strip(),nivel.strip())

    def show_data(self):
        response={
            "Nombre de la responsabilidad: ": self.get_nombre(),
            "Prioridad del cargo(Nivel 1: baja, Nivel 10: alta)": self.get_nivel()
        }
        json_response=json.dumps(response)
        return json_response
    #endregion

    

    