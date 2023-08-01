import json

class Divisa():
    #region constructor
    def __init__(self,simbolo,descripcion_moneda,valor,valor_mostrar):
        self.simbolo=simbolo
        self.descripcion_moneda=descripcion_moneda
        self.valor=valor
        self.valor_mostrar=None #It will update in the setter
    #endregion

    #region getter
    def get_simbolo(self):
        return self.simbolo
    
    def get_descripcion_moneda(self):
        return self.descripcion_moneda
    
    def get_valor(self):
        return self.valor
    
    def get_valor_mostrar(self):
        return self.valor_mostrar
    #endregion

    #region setter
    def set_simbolo(self, new_symbol):
        self.simbolo=new_symbol

    def set_descripcion_moneda(self, new_description_currency):
        self.descripcion_moneda=new_description_currency
    
    def set_valor(self, new_value):
        self.valor=new_value
    
    "Evaluates the description to define the symbol and the currency value."
    def set_valor_mostrar(self, simbolo ,valor):
        self.valor_mostrar=(f"{simbolo}{valor:,.0f}" if self.descripcion_moneda in ["Guarani","Guaranies"]
                            else f"{simbolo}{valor:,.2f}")
    
    #endregion

    #region methods

    @classmethod
    def crate_from_string(cls,data_string):
        simbolo, descripcion_moneda,valor,valor_mostrar=data_string.split(",")
        return cls(simbolo.strip(),descripcion_moneda.strip(),valor.strip(),valor_mostrar.strip())
    
    @classmethod
    def show_data(cls, divisa):
        response={
            "Descripción: ": divisa.get_descripcion_moneda(),
            "Monto: ": divisa.get_valor_mostrar()
        }
        json_response=json.dumps(response)
        return json_response
    #endregion
    

    
