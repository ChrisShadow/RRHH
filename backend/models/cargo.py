from models.divisa import Divisa
from models.lista_actividades import ListaActividades
from models.lista_horario import ListaHorario

import json


# region Doc

# Some definitions
"""Class->a template.
Attribute->A variable within a class.
Method->A function within a class.
Object->A particular instance of a class.
Constructor->Code that runs when an object is created.
Inheritance->The ability to extend a class to make a new class."""

# Fundamental elements
"""Inheritance: Adoption of properties from the parent class into the child class.
Polymorphism: Creation of many forms from one form.
Abstraction: Displaying the necessary data and hiding unnecessary data.
Encapsulation: Securing the info of the class."""

# Classes in Python
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

# Class attributes:
"""If attributes are constant and do not change between different instances of the Cargo class, it is appropriate to define them as class attributes.
They are shared between all instances of the class, which can save memory and avoid redundancy if the values are the same for all instances."""

# Instance attributes:
"""If attributes are specific to each instance of the Cargo class and can change from one instance to another, they must be defined as instance attributes.
They are initialised when a new instance of the class is created and belong exclusively to that instance."""

# Resources
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

# endregion


class Cargo():
    # region class attibutes
    """This defines two dictionaries, TIPOFUNCIONARIO and PERIODOPAGO, 
    which map integer keys to string values representing types of 
    employees and pay periods, respectively."""

    TIPOFUNCIONARIO = {1: 'Asalariado', 2: 'Tercerizado'}
    PERIODOPAGO = {1: 'Jornal', 2: 'Semanal', 3: 'Quincenal', 4: 'Mensual'}
    # endregion

    # region constructor
    """The code defines a class called "Cargo" with an initializer that takes 
    several parameters. It initializes various attributes of the class and also 
    checks the validity of some input values. The class has vertical and 
    horizontal relationship attributes represented as lists."""

    def __init__(self, name, lista_actividad, lista_horario, divisa, indice_tipo_funcionario, pago_funcionario, porcentaje_comision,
                 indice_periodo_pago):
        self.name = name
        # as a parameter of assigned instance of lista_actividad #ListaActividades() as created instance for each Cargos' instance
        self._lista_actividad = lista_actividad
        self._lista_horario = lista_horario  # ListaHorario()
        self._divisa = divisa  # Divisa
        self.check_indice_tipo_funcionario(indice_tipo_funcionario)
        self.indice_tipo_funcionario = indice_tipo_funcionario
        self.pago_funcionario = pago_funcionario
        self.porcentaje_comision = porcentaje_comision
        self.check_indice_periodo_pago(indice_periodo_pago)
        self.indice_periodo_pago = indice_periodo_pago

        # Vertical relationships (top and bottom)
        self._relacion_v_arriba = []  # as an empty list
        self._relacion_v_abajo = []  # as an empty list
        # Horizontaal relationships (positions at the same level)
        self._relacion_horizontal = []  # as an empty list
    # endregion

    # region getter
    """It defines a class called "Cargo" with various methods to retrieve 
    different attributes and relationships associated with a cargo. 
    The methods allow access to the cargo's name, list of activities, 
    list of schedules, currency, payment for employees, commission percentage, 
    type of employee, payment period, and relationships with other cargos."""

    def get_name(self):
        return self.name

    # show_data displays the attributes of the accessed class
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
        return Cargo.TIPOFUNCIONARIO[self.get_indice_tipo_funcionario()]

    def get_indice_periodo_pago(self):
        return self.indice_periodo_pago

    def get_periodo_pago(self):
        return Cargo.PERIODOPAGO[self.get_indice_periodo_pago()]

    """For obtaining the relations"""

    def get_relacion_v_arriba(self):
        return [cargo.get_name() for cargo in self._relacion_v_arriba]

    def get_relacion_v_abajo(self):
        return [cargo.get_name() for cargo in self._relacion_v_abajo]

    def get_relacion_horizontal(self):
        return [cargo.get_name() for cargo in self._relacion_horizontal]

    # endregion

    # region setter
    """IT defines a class named "cargo" and includes several setter methods 
    to set various attributes of the cargo object. These attributes include name, 
    vertical relationships (above and below), horizontal relationship, 
    activity list, schedule list, currency, payment for the employee, 
    commission percentage, type of employee index, and payment period index. 
    It also includes commented out setter methods that are not required 
    due to the absence of necessary changes in the dictionary."""

    def set_name(self, new_name):
        self.name = new_name

    def set_relacion_v_arriba(self, new_relacion_v_arriba):
        self._relacion_v_arriba = new_relacion_v_arriba

    def set_relacion_v_abajo(self, new_relacion_v_abajo):
        self._relacion_v_abajo = new_relacion_v_abajo

    def set_relacion_horizontal(self, new_relacion_horizontal):
        self._relacion_horizontal = new_relacion_horizontal

    def set_lista_actividad(self, new_lista_actividad):
        self._lista_actividad = new_lista_actividad

    def set_lista_horario(self, new_lista_horario):
        self._lista_horario = new_lista_horario

    def set_divisa(self, new_divisa):
        self._divisa = new_divisa

    def set_pago_funcionario(self, new_pago_funcionario):
        self.pago_funcionario = new_pago_funcionario

    def set_porcentaje_comision(self, new_porcentaje_comision):
        self.porcentaje_comision = new_porcentaje_comision

    def set_indice_tipo_funcionario(self, new_indice_tipo_funcionario):
        self.check_indice_tipo_funcionario(new_indice_tipo_funcionario)
        self.indice_tipo_funcionario = new_indice_tipo_funcionario

    def set_indice_periodo_pago(self, new_indice_periodo_pago):
        self.check_indice_periodo_pago(new_indice_periodo_pago)
        self.indice_periodo_pago = new_indice_periodo_pago

    "It is not required because changes won't be necessary in the dict"
    # def set_tipo_funcionario(self,new_tipo_funcionario):
    #    for key, value in self.tipo_funcionario.items():
    #        if value==new_tipo_funcionario:
    #            self.indice_tipo_funcionario=key
    #            break

    # def set_indice_periodo_pago(self,new_indice_periodo_pago):
    #    for key, value in self.indice_periodo_pago.items():
    #        if value==new_indice_periodo_pago:
    #            self.indice_periodo_pago=key
    #            break

    # endregion

   # region class methods
    """It defines a function called  check_indice_tipo_funcionario  which takes 
    two parameters:  self  and  indice_tipo_funcionario . It checks if the  
    indice_tipo_funcionario  is a valid index in the  TIPOFUNCIONARIO  list. 
    If it is not valid, it prints a message indicating that the index is invalid."""

    def check_indice_tipo_funcionario(self, indice_tipo_funcionario):
        if indice_tipo_funcionario not in self.TIPOFUNCIONARIO:
            print("Índice de tipo de funcionario no válido.")

    """It defines a function called  check_indice_periodo_pago  which takes 
    two parameters:  self  and  indice_periodo_pago . It checks if the  
    indice_periodo_pago  is a valid index in the  PERIODOPAGO  list. 
    If it is not valid, it prints a message indicating that the index is invalid."""

    def check_indice_periodo_pago(self, indice_periodo_pago):
        if indice_periodo_pago not in self.PERIODOPAGO:
            print("Índice de periodo de pago no válido.")

    """The code defines a class named "cargo" with two class methods. 
    The first method, "get_tipo_funcionario_dict", returns a dictionary called 
    "TIPOFUNCIONARIO". The second method, "get_periodo_pago_dict", returns 
    a dictionary called "PERIODOPAGO"."""
    @classmethod
    def get_tipo_funcionario_dict(cls):
        return cls.TIPOFUNCIONARIO

    @classmethod
    def get_periodo_pago_dict(cls):
        return cls.PERIODOPAGO

    # Methods for adding charges to relationships
    def add_relacion_v_arriba(self, cargo):
        self._relacion_v_arriba.append(cargo)

    def add_relacion_v_abajo(self, cargo):
        self._relacion_v_abajo.append(cargo)

    def add_relacion_horizontal(self, cargo):
        self._relacion_horizontal.append(cargo)

    # Methods to remove charges from relationships
    def delete_relacion_v_arriba(self, cargo):
        if cargo in self._relacion_v_arriba:
            self._relacion_v_arriba.remove(cargo)

    def delete_relacion_v_abajo(self, cargo):
        if cargo in self._relacion_v_abajo:
            self._relacion_v_abajo.remove(cargo)

    def delete_relacion_horizonta(self, cargo):
        if cargo in self._relacion_horizontal:
            self._relacion_horizontal.remove(cargo)

    """This defines a method called "to_dict" within a class. The method converts 
    the object's attributes into a dictionary and returns it, along with additional 
    information, such as the type of employee and their remuneration. 
    The method also calculates the total payment amount and formats it based on 
    the currency. The returned dictionary contains various details about 
    the cargo (position) such as name, vertical and horizontal relationships, 
    activity list, schedule list, commission percentage, currency, payment period, 
    and payment amount."""

    def to_dict(self):
        divisa_info = Divisa.show_data(self._divisa)
        divisa_data = json.loads(divisa_info)

        "In order to determine: Tipo de funcionario y remuneración"
        tipo_funcionario = (f"{self.get_tipo_funcionario()}/" +
                            f"Salario: {self.get_pago_funcionario():,.2f}" if self.get_indice_tipo_funcionario() == 1
                            else f"{self.get_tipo_funcionario()}/" +
                            f"Viático: {self.get_pago_funcionario():,.2f}"
                            )
        monto_total = ((self.get_pago_funcionario(
        )*self.get_porcentaje_comision())/100)+self.get_pago_funcionario()
        pago_funcionario_info = (
            f"{divisa_data['Simbolo: ']}{monto_total:,.0f}"
            if divisa_data["Descripcion: "] in ["Guarani", "Guaranies"]
            else f"{divisa_data['Simbolo: ']}{monto_total:,.2f}"
        )

        "The response will be a tuple containing the dictionary as the first element and the JSON string as the second element."
        return {
            "Nombre del cargo: ": self.get_name(),
            "Relación vertical arriba: ": self.get_relacion_v_arriba(),
            "Relación vertical abajo: ": self.get_relacion_v_abajo(),
            "Relación horizontal: ": self.get_relacion_horizontal(),
            "Lista de actividades(Nombre y prioridad): ": self.get_lista_actividad(),
            "Lista de horario(Lugar y días más horas): ": self.get_lista_horario(),
            "Tipo de funcionario y remuneración: ": tipo_funcionario,
            "Porcentaje Comisión: ": self.get_porcentaje_comision(),
            "Moneda: ":  divisa_data["Descripcion: "],
            "Período Pago: ": self.get_periodo_pago(),
            "Monto Pago Funcionario: ": pago_funcionario_info
        }

    """It defines a method called show_data that converts a dictionary into 
    a JSON string using the json.dumps() function."""

    def show_data(self):
        data_dict = self.to_dict()
        "dumps() of the json module takes the dictionary as input and returns a text string in JSON format"
        json_response = json.dumps(data_dict)
        return json_response
   # endregion
