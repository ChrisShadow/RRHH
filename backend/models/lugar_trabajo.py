import json


class LugarTrabajo():

    # region construct
    """ The class has attributes to store the name of the company, branch, city, and location."""

    def __init__(self, nombre_empresa, sucursal, ciudad, ubicacion):
        self.nombre_empresa = nombre_empresa
        self.sucursal = sucursal
        self.ciudad = ciudad
        self.ubicacion = ubicacion
    # endregion

    # region getter
    """These methods retrieve information about a workplace, such as the name of the company, the branch, the city, and the location."""

    def get_nombre_empresa(self):
        return self.nombre_empresa

    def get_sucursal(self):
        return self.sucursal

    def get_ciudad(self):
        return self.ciudad

    def get_ubicacion(self):
        return self.ubicacion
    # endregion

    # region setter
    """These methods set the name of a business, its branch, city, and location"""

    def set_nombre_empresa(self, new_name_business):
        self.nombre_empresa = new_name_business

    def set_sucursal(self, new_branch):
        self.sucursal = new_branch

    def set_ciudad(self, new_city):
        self.ciudad = new_city

    def set_ubicacion(self, new_location):
        self.ubicacion = new_location
    # endregion

    # region methods
    """It defines a class method that creates an instance of the class 
    "LugarTrabajo" from a string input. The string input is expected to 
    contain comma-separated values for the name of the company, its branch, 
    city, and location. The method splits the string and creates an instance 
    of the class with the stripped values."""
    @classmethod
    def create_from_string(cls, data_string):
        nombre_empresa, sucursal, ciudad, ubicacion = data_string.split(",")
        return cls(nombre_empresa.strip(), sucursal.strip(), ciudad.strip(), ubicacion.strip())

    """It defines a class method  show_data  in the  LugarTrabajo  class. This 
    method takes a  lugar_trabajo  object as input and returns a JSON response 
    containing information about the workplace. The response includes the 
    company name, branch, city, and location. The  json  module is used to 
    convert the response dictionary into a JSON string."""
    @classmethod
    def show_data(cls, lugar_trabajo):
        response = {
            "Empresa: ": lugar_trabajo.get_nombre_empresa(),
            "Sucursal: ": lugar_trabajo.get_sucursal(),
            "Ciudad: ": lugar_trabajo.get_ciudad(),
            "Ubicacion: ": lugar_trabajo.get_ubicacion()
        }
        json_response = json.dumps(response)
        return json_response

    # It will be used as a key in the dictionary in show_data of class ListaHorario.
    def get_empresa_sucursal_combination(self):
        return f"{self.get_nombre_empresa()}, {self.get_sucursal()}"

    # endregion
