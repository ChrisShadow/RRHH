import json
class LugarTrabajo():

    #region construct
    def __init__(self,nombre_empresa,sucursal,ciudad,ubicacion):
        self.nombre_empresa=nombre_empresa
        self.sucursal=sucursal
        self.ciudad=ciudad
        self.ubicacion=ubicacion
    #endregion

    #region getter
    def get_nombre_empresa(self):
        return self.nombre_empresa

    def get_sucursal(self):
        return self.get_sucursal
    
    def get_ciudad(self):
        return self.ciudad
    
    def get_ubicacion(self):
        return self.ubicacion
    #endregion

    #region setter
    def set_nombre_empresa(self,new_name_business):
        self.nombre_empresa=new_name_business

    def set_sucursal(self, new_branch):
        self.sucursal=new_branch

    def set_ciudad(self,new_city):
        self.ciudad=new_city
    
    def set_ubicacion(self,new_location):
        self.ubicacion=new_location
    #endregion

    #region methods
    @classmethod
    def crate_from_string(cls, data_string):
        nombre_empresa, sucursal, ciudad, ubicacion = data_string.split(
            ",")
        return cls(nombre_empresa.strip(), sucursal.strip(), ciudad.strip(), ubicacion.strip())

    @classmethod
    def show_data(cls, lugar_trabajo):
        response = {
            "Empresa: ": lugar_trabajo.get_nombre_empresa(),
            "Sucursal: ": lugar_trabajo.get_sucursal() ,
            "Ciudad: ": lugar_trabajo.get_ciudad(),
            "Ubicación: ":lugar_trabajo.get_ubicacion()
        }
        json_response = json.dumps(response)
        return json_response
    
    #It will be used as a key in the dictionary horarios_dict in show_horarios_por_lugar of class ListaHorario.
    def get_empresa_sucursal_combination(self):
        return f"{self.get_nombre_empresa() - {self.get_sucursal()}}"
    #endregion
