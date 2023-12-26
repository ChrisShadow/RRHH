import json


class Divisa():
    # region constructor
    """It defines a class called "divisa" with an initializer that takes ç
    in parameters for the currency symbol, currency description, and currency 
    value. It also has an optional parameter for the displayed value. If the 
    displayed value is not provided, it is set using the currency symbol 
    and value."""

    def __init__(self, simbolo, descripcion_moneda, valor, valor_mostrar=None):
        self.simbolo = simbolo
        self.descripcion_moneda = descripcion_moneda
        self.valor = valor
        # self.valor_mostrar = valor_mostrar  # It will update in the setter

        if valor_mostrar is None:
            self.set_valor_mostrar(simbolo, valor)
        else:
            self.valor_mostrar = valor_mostrar

    # endregion

    # region getter
    """These methods return the values of the corresponding attributes of the class."""

    def get_simbolo(self):
        return self.simbolo

    def get_descripcion_moneda(self):
        return self.descripcion_moneda

    def get_valor(self):
        return self.valor

    def get_valor_mostrar(self):
        return self.valor_mostrar
    # endregion

    # region setter
    """This code defines a class Divisa with methods to set the symbol, 
    currency description, and value. It also includes a method to evaluate 
    the currency description and set the currency value to be displayed 
    accordingly."""

    def set_simbolo(self, new_symbol):
        self.simbolo = new_symbol

    def set_descripcion_moneda(self, new_description_currency):
        self.descripcion_moneda = new_description_currency

    def set_valor(self, new_value):
        self.valor = new_value

    "It evaluates the description to define the symbol and the currency value."

    def set_valor_mostrar(self, simbolo, valor):
        self.valor_mostrar = (f"{simbolo}{valor:,.0f}" if self.descripcion_moneda in ["Guarani", "Guaranies"]
                              else f"{simbolo}{valor:,.2f}")

    # endregion

    # region methods
    """This defines a class method called "create_from_string" which takes 
    a data string as input. The data string is expected to be in the format 
    "symbol, currency_description, value". The method splits the string using 
    commas as the delimiter and assigns the split values to variables. It then 
    returns an instance of the class with the stripped and converted values."""
    @classmethod
    def create_from_string(cls, data_string):
        simbolo, descripcion_moneda, valor, = data_string.split(
            ",")
        return cls(simbolo.strip(), descripcion_moneda.strip(), float(valor.strip()))

    """It defines a class method called "show_data" that takes a "divisa" 
    object as input. It retrieves the symbol, description, and value of the 
    currency from the "divisa" object and creates a JSON response containing 
    this information. The JSON response is then returned."""
    @classmethod
    def show_data(cls, divisa):
        response = {
            "Simbolo: ": divisa.get_simbolo(),
            "Descripcion: ": divisa.get_descripcion_moneda(),
            "Monto: ": divisa.get_valor_mostrar()
        }
        json_response = json.dumps(response)
        return json_response
    # endregion
