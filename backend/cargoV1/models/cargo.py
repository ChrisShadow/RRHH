from divisa import Divisa
from lista_actividades import ListaActividades
from lista_horario import ListaHorario
from rela_v_abajo import RelacionVAbajo
from rela_v_arriba import RelacionVArriba
from relacion_Horiz import RelacionHorizontal

import json



#region Doc

#Some definitions
"""Class->a template.
Attribute->A variable within a class.
Method->A function within a class.
Object->A particular instance of a class.
Constructor->Code that runs when an object is created.
Inheritance->The ability to extend a class to make a new class."""

#Fundamental elements
"""Inheritance: Adoption of properties from the parent class into the child class.
Polymorphism: Creation of many forms from one form.
Abstraction: Displaying the necessary data and hiding unnecessary data.
Encapsulation: Securing the info of the class."""

#Classes in Python 
"""They are created with the keyword class, followed by the name of the class. Class attributes are defined after the class- 
-name, and they are shared by all instances of the class. Individual instance attributes are defined after the class attributes, and-
-they are unique to each instance. Method definitions are also placed after the class definition. Methods are functions that are-
-associated with a class, and they are used to process or manipulate the data stored in instances of the class.
In Python we have class type attributes and instance type attributes:
That is, those not defined in the constructor(__init__) and those that are defined in it.
The same ocurrs with methods: class level ones and instance level ones. Key word are self for the-
-instance level and cls for class level."
Another kind of method is the static one. Only has access to the parameters that we pass into it individually and then-
-can be used with either the class itself or the instance object.
There are not private and protected, just public and non-public(uses __ for att and meth) class members.
Basic Decorations: @classmethod, @staticmethod
Classes inside another classes: Inner Classes
Functions inside another functions: nested methods"""

#Class attributes:
"""If attributes are constant and do not change between different instances of the Cargo class, it is appropriate to define them as class attributes.
They are shared between all instances of the class, which can save memory and avoid redundancy if the values are the same for all instances."""

#Instance attributes:
"""If attributes are specific to each instance of the Cargo class and can change from one instance to another, they must be defined as instance attributes.
They are initialised when a new instance of the class is created and belong exclusively to that instance."""

#Resources
"""classes on Python: https://docs.python.org/3/tutorial/classes.html"
https://youtu.be/LwFnF9XoEfM
https://realpython.com/lessons/managing-class-attributes/
https://www.geeksforgeeks.org/python-classes-and-objects/
https://realpython.com/python-namespaces-scope/#:~:text=the%20next%20level.-,Namespaces%20in%20Python,values%20are%20the%20objects%20themselves.
https://www.askpython.com/python/oops/class-instance-attributes#:~:text=You%20can%20access%20the%20attributes,would%20use%20the%20expression%20myClass.
Modules and Packages: https://youtu.be/f26nAmfJggw
Public and private classes: https://youtu.be/xY__sjI5yVU
Public and Private members: https://youtu.be/js9EITv4HqM
Passign members from one class to another one: https://youtu.be/iDc_VrawjqY"""

#endregion


class Cargo():
    "static variables: those which are not from other classes"
    #region class attibutes
    tipo_funcionario={1:'Asalariado',2:'Tercerizado'}
    periodo_pago={1:'Jornal',2:'Semanal',3:'Quincenal',4:'Mensual'}
    #endregion

    """Constructor lets the class initialize the object's attributes and serves no other purpose"""
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

    "All get functions retrieve the instance attributes, individually"
    #region getter
    def get_name(self):
        return self.name
    
    """Here, the method show_data in RelacionVArriba displays the attributes as a whole in itself is accessed. 
    Basically the same with the others classes."""
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

    "All set functions enable to change of the values of those attributes,individually"
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
    """Here, the dictionary tipo_funcionario is obtained directly using the class name, Cargo."
    Class-exclusive method, since tipo_funcionario is of class type. The same with periodo_pago"""
    @classmethod
    def get_tipo_funcionario_dict(cls):
        return cls.tipo_funcionario

    @classmethod
    def get_periodo_pago_dict(cls):
        return cls.periodo_pago

    "Display the data as a whole transformed as a json object in order send to the view as a json object."
    def show_data(self):
        
        "In order to determine: Tipo de funcionario y remuneración"
        tipo_funcionario=(f"Tipo funcionario: {self.get_tipo_funcionario()} " + 
                          f"Salario: {self.get_pago_funcionario()}" if self.indice_tipo_funcionario==1 
                          else f"Tipo funcionario: {self.get_tipo_funcionario()} " + 
                          f"Viático: {self.get_pago_funcionario()}"
                          )
        
        "The response will be a tuple containing the dictionary as the first element and the JSON string as the second element."
        response= {
            "Nombre del cargo: ": self.get_name(),
            "Relación vertical arriba: ": self.get_relacion_v_arriba(), 
            "Relación vertical abajo: ": self.get_relacion_v_abajo(),
            "Relación horizontal: ": self.get_relacion_horizontal(),
            "Lista de actividades: ":self.get_lista_actividad(),
            "Lista de horario: ": self.get_lista_horario(),
            "Tipo de funcionario y remuneración: ":tipo_funcionario,
            "Porcentaje Comisión: ": self.get_porcentaje_comision(),
            "Moneda: ": self.get_divisa(),
            "Período Pago: ": self.get_periodo_pago()
            }

        "dumps() of the json module takes the dictionary as input and returns a text string in JSON format"
        json_response=json.dumps(response)
        return json_response
   #endregion