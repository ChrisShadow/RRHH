from divisa import Divisa
from lista_actividades import ListaActividades
from lista_horario import ListaHorario
from rela_v_abajo import RelacionVAbajo
from rela_v_arriba import RelacionVArriba
from relacion_Horiz import RelacionHorizontal



#region Doc

#Inheritance: Adoption of properties from the parent class into the child class.
#Polymorphism: Creation of many forms from one form.
#Abstraction: Displaying the necessary data and hiding unnecessary data.
#Encapsulation: Securing the info of the class.
"Classes in Python are created with the keyword class, followed by the name of the class. Class attributes are defined after the class-" 
"-name, and they are shared by all instances of the class. Individual instance attributes are defined after the class attributes, and-" 
"-they are unique to each instance. Method definitions are also placed after the class definition. Methods are functions that are-"
"-associated with a class, and they are used to process or manipulate the data stored in instances of the class."

"classes on Python: https://docs.python.org/3/tutorial/classes.html"
"https://youtu.be/LwFnF9XoEfM"
"https://realpython.com/lessons/managing-class-attributes/"
"https://www.geeksforgeeks.org/python-classes-and-objects/"
"https://realpython.com/python-namespaces-scope/#:~:text=the%20next%20level.-,Namespaces%20in%20Python,values%20are%20the%20objects%20themselves."
"https://www.askpython.com/python/oops/class-instance-attributes#:~:text=You%20can%20access%20the%20attributes,would%20use%20the%20expression%20myClass."
"Modules and Packages: https://youtu.be/f26nAmfJggw"
"Public and private classes: https://youtu.be/xY__sjI5yVU"
"Public and Private members: https://youtu.be/js9EITv4HqM"

"There are not private and protected, just public and non-public(uses __ for att and meth) class members"
"Passign members from one class to another one: https://youtu.be/iDc_VrawjqY"
"Basic Decorations: @classmethod, @staticmethod"
"Classes inside another classes: Inner Classes"
"Functions inside another functions: nested methods"

#In Python we have class type attributes and instance type attributes. 
# That is, those not defined in the constructor(__init__) and those that are defined in it.
#The same ocurrs with methods: class level ones and instance level ones. Key word are self for the 
#instance level and cls for class level
#Another kind of method is the static one. Only has access to the parameters that we pass into it individually and then
#can be used with either the class itself or the instance object
#endregion

class Cargo():
    "static variables: those which are not from other classes"
    #region class attibutes
    "Dictionary type variable constant "
    tipo_funcionario={1:'Asalariado',2:'Tercerizado'}
    periodo_pago={1:'Jornal',2:'Semanal',3:'Quincenal',4:'Mensual'}
    #endregion

    "It is called every time an object is created from a class and lets the class initialize the object's attributes and serves no other purpose"
    "self keyword to make sure that the properties are properly bound to the class. There is no use of class declaration if we do not use the self keyword"
    "Those which have _X, it is due to non-public member: from another class"
    #region constructor
    def __init__(self,name,relacion_v_arriba,relacion_v_abajo,relacion_horizontal,lista_actividad,lista_horario,divisa,indice_tipo_funcionario,pago_funcionario,porcentaje_comision,
                 indice_periodo_pago):
        self.name=name
        self._relacion_v_arriba=relacion_v_arriba
        self._relacion_v_abajo=relacion_v_abajo
        self._relacion_horizontal=relacion_horizontal
        self._lista_actividad=lista_actividad
        self._lista_horario=lista_horario
        self._divisa=divisa
        self.indice_tipo_funcionario=indice_tipo_funcionario
        self.pago_funcionario=pago_funcionario
        self.porcentaje_comision=porcentaje_comision
        self.indice_periodo_pago=indice_periodo_pago
    #endregion

    "Retrieves the instance attributes."
    #region getter
    def get_name(self):
        return self.name
    
    "Here, the method that displays the attributes as a whole in RelacionVArriba is accessed"
    def get_relacion_v_arriba(self):
        return RelacionVArriba.show_data(self._relacion_v_arriba)
    
    def get_relacion_v_abajo(self):
        return RelacionVAbajo.show_data(self._relacion_v_abajo) 
    
    def get_relacion_horizontal(self):
        return RelacionHorizontal.show_data(self._relacion_horizontal) 
    
    def get_lista_actividad(self):
        return ListaActividades.show_data(self._lista_actividad)
    
    def get_lista_horario(self):
        return ListaHorario.show_data(self._lista_horario)
    
    def get_divisa(self):
        return Divisa.show_data(self._divisa)
    
    def get_pago_funcionario(self):
        return self.pago_funcionario
    
    def get_porcentaje_comision(self):
        return self.porcentaje_comision

    "Additional method to get the indexes and then access the values in the tipo_funcionario dictionary"
    def get_indice_tipo_funcionario(self):
        return self.indice_tipo_funcionario

    "Here if the indices change, the values you obtain using get_indice_tipo_funcionario() will also change automatically."
    def get_tipo_funcionario(self):
        return Cargo.tipo_funcionario[self.get_indice_tipo_funcionario()]
    
    def get_indice_periodo_pago(self):
        return self.indice_periodo_pago

    def get_periodo_pago(self):
        return Cargo.periodo_pago[self.get_indice_periodo_pago()]
    
    #endregion

    "Enables to change of the values of those attributes"
    #region setter
    def set_name(self, new_name):
        self.name=new_name
    
    def set_relacion_v_arriba(self,new_relacion_v_arriba):
        self._relacion_v_arriba=new_relacion_v_arriba

    def set_relacion_v_abajo(self,new_relacion_v_abajo):
        self._relacion_v_abajo=new_relacion_v_abajo

    def set_relacion_horizontal(self,new_relacion_horizontal):
        self._relacion_horizontal=new_relacion_horizontal

    def set_lista_actividad(self,new_lista_actividad):
        self._lista_actividad=new_lista_actividad

    def set_lista_horario(self,new_lista_horario):
        self._lista_horario=new_lista_horario


    def set_divisa(self,new_divisa):
        self._divisa=new_divisa
    
    def set_pago_funcionario(self, new_pago_funcionario):
        self.pago_funcionario=new_pago_funcionario
    
    def set_porcentaje_comision(self,new_porcentaje_comision):
        self.porcentaje_comision=new_porcentaje_comision
    
    def set_indice_tipo_funcionario(self,new_indice_tipo_funcionario):
        self.indice_tipo_funcionario=new_indice_tipo_funcionario

    "It is not required because changes won't be necessary in the dict"
    #def set_tipo_funcionario(self,new_tipo_funcionario):
    #    for key, value in self.tipo_funcionario.items():
    #        if value==new_tipo_funcionario:
    #            self.indice_tipo_funcionario=key
    #            break
    
    def set_indice_periodo_pago(self,new_indice_periodo_pago):
        self.indice_periodo_pago=new_indice_periodo_pago

    #def set_indice_periodo_pago(self,new_indice_periodo_pago):
    #    for key, value in self.indice_periodo_pago.items():
    #        if value==new_indice_periodo_pago:
    #            self.indice_periodo_pago=key
    #            break

    
    
    #endregion

   #region class methods
   #"Here, the dictionary tipo_funcionario is obtained directly using the class name, Cargo."
    @classmethod
    def get_tipo_funcionario_dict(cls):
        return cls.tipo_funcionario

    @classmethod
    def get_periodo_pago_dict(cls):
        return cls.periodo_pago

   #endregion