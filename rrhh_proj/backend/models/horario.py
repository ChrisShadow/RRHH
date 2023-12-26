import json
import re


class Horario():

    # region constructor
    """ It defines a class called "horario" which represents a schedule. 
    The class has three attributes: "dias" (days), "hora_inicio" (start time),
    and "hora_fin" (end time). The  __init__  method is used to initialize
    these attributes."""

    def __init__(self, dias=None, hora_inicio=None, hora_fin=None):
        self.dias = dias
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
    # endregion

    # region getter
    """These methods return the values of the corresponding attributes of the class."""

    def get_dias(self):
        return self.dias

    def get_hora_inicio(self):
        return self.hora_inicio

    def get_hora_fin(self):
        return self.hora_fin
    # endregion

    # region setter
    """This code is used to set the days for a schedule. It accepts a list 
    of days as input and checks if all the days entered are valid. If they 
    are valid, it updates the value of the "_days" attribute. If any duplicates
    or invalid days are found, it generates appropriate error messages. If no 
    valid days are found, it sets "Monday" as the default day."""

    def set_dias(self, new_days_string):
        # Valid only days list
        dias_posibles = ["Lunes", "Martes", "Miercoles",
                         "Jueves", "Viernes", "Sabado", "Domingo"]

        # Divides the string into days using commas as separators
        new_days = new_days_string.split(",")
        # Remove duplicates and validate days
        unique_dias = []  # List to store unique days
        duplicate_dias = []  # List to store duplicated days
        invalid_dias = []  # List to store invalid days

        for dia in new_days:
            dia_stripped = dia.strip()

            if dia_stripped in unique_dias:
                # Duplicate day found, we add it to the list of duplicates.
                duplicate_dias.append(dia_stripped)
            elif dia_stripped in dias_posibles:
                # We add only if it is a valid day
                unique_dias.append(dia_stripped)
            else:
                # Invalid day found, we add it to the invalid list.
                invalid_dias.append(dia_stripped)

        if duplicate_dias:
            print(f"Días duplicados eliminados: {', '.join(duplicate_dias)}")

        if invalid_dias:
            print(
                f"Día(s) no válido(s) encontrados: {', '.join(invalid_dias)}")

        if not unique_dias:
            # If there are no valid single days, set "Monday" as the default day.
            unique_dias = ["Lunes(default)"]

        self.dias = unique_dias
        """"By using "return self" in a method, we are simply returning the 
        current instance of the class to the caller. This can be useful in 
        certain situations, such as when we want to chain method calls 
        together on the same object."""
        return self

    """It defines a method to set the starting hour of a schedule. It 
    validates the input time format using a regular expression pattern. If 
    the format is valid, it sets the starting hour. Otherwise, it prints an 
    error message and sets a default starting hour of '08:00(Default)'."""

    def set_hora_inicio(self, new_starting_hour):
        # Defines a regular expression pattern to validate the time format
        hora_patron = r"^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$"

        if re.match(hora_patron, new_starting_hour):
            self.hora_inicio = new_starting_hour
        else:
            # raise ValueError("El formato de la hora no es válido. Debe ser ##:##.")
            print("El formato de la hora inicio no es válido. Debe ser ##:##.")
            self.hora_inicio = '08:00(Default)'
        """to chain method calls together on the same object."""
        return self

    def set_hora_fin(self, new_leaving_hour):
        # Defines a regular expression pattern to validate the time format
        hora_patron = r"^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$"

        if re.match(hora_patron, new_leaving_hour):
            self.hora_fin = new_leaving_hour
        else:
            # raise ValueError("El formato de la hora no es válido. Debe ser ##:##.")
            print("El formato de la hora fin no es válido. Debe ser ##:##.")
            self.hora_fin = '17:00(Default)'
        """to chain method calls together on the same object."""
        return self

    # endregion

    # region methods
    """It takes a data string as input. The code splits the data string into 
    different parts and extracts the values. It then validates the days 
    mentioned in the data string, removes duplicates, and identifies any 
    invalid days. If there are no valid single days, it sets "Monday" as 
    the default day. The code also validates the time format for the start
    and end times and provides default values if the format is invalid. 
    Finally, it returns the unique days, start time, and end time."""
    @classmethod
    def _process_data_string(cls, data_string):
        # Dividing the chain into parts
        parts = data_string.split(',')

        # Extract the values
        dias = parts[:-2]  # Get a list of days (all but the last two)
        hora_inicio = parts[-2]
        hora_fin = parts[-1]

        # Validate the days
        dias_posibles = ["Lunes", "Martes", "Miercoles",
                         "Jueves", "Viernes", "Sabado", "Domingo"]

        # Remove duplicates and validate days
        unique_dias = []  # List to store unique days
        duplicate_dias = []  # List to store duplicated days
        invalid_dias = []  # List to store invalid days
        for dia in dias:
            dia_stripped = dia.strip()
            if dia_stripped in unique_dias:
                # Duplicate day found, we add it to the list of duplicates.
                duplicate_dias.append(dia_stripped)
            elif dia_stripped in dias_posibles:
                # We add only if it is a valid day
                unique_dias.append(dia_stripped)
            else:
                # Invalid day found, we add it to the invalid list.
                invalid_dias.append(dia_stripped)

        if duplicate_dias:
            print(f"Días duplicados eliminados: {', '.join(duplicate_dias)}")

        if invalid_dias:
            print(
                f"Día(s) no válido(s) encontrados: {', '.join(invalid_dias)}")

        if not unique_dias:
            # If there are no valid single days, set "Monday" as the default day.
            unique_dias = ["Lunes(default)"]

        # Defines a regular expression pattern to validate the time format
        hora_patron = r"^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$"

        if not re.match(hora_patron, hora_inicio):
            # raise ValueError("El formato de la hora no es válido. Debe ser ##:##.")
            print("El formato de la hora inicio no es válido. Debe ser ##:##.")
            hora_inicio = '08:00(Default)'

        if not re.match(hora_patron, hora_fin):
            # raise ValueError("El formato de la hora no es válido. Debe ser ##:##.")
            print("El formato de la hora fin no es válido. Debe ser ##:##.")
            hora_fin = '17:00(Default)'

        return unique_dias, hora_inicio.strip(), hora_fin.strip()

    """It defines a class method  create_from_string  that takes a data string
    as input and creates an instance of the class with the specified values. 
    The data string is processed to extract the days, start time, and end time,
    and then used to create the instance."""
    @classmethod
    def create_from_string(cls, data_string):
        # Create an instance and assign the values
        dias, hora_inicio, hora_fin = cls._process_data_string(data_string)
        return cls(dias, hora_inicio, hora_fin)

    """It defines a function called 'update_from_string' which takes a data string
    as input and updates the 'dias', 'hora_inicio', and 'hora_fin' attributes 
    of an object. The function first processes the data string using the 
    '_process_data_string' method and assigns the extracted values to the 
    respective attributes."""

    def update_from_string(self, data_string):
        dias, hora_inicio, hora_fin = self._process_data_string(data_string)
        self.dias = dias
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    # @classmethod
    """It defines a function  show_data  that returns a JSON response containing
    information about a schedule. It retrieves the days, start time, and end 
    time of the schedule and formats them into a dictionary. 
    The dictionary is then converted to a JSON string using the  json.dumps  
    function before being returned."""

    def show_data(self):  # horario
        # days = horario.get_dias()
        # days_combined = ", ".join(days)  # Joining days with a comma and a space
        response = {
            "Dias: ": ", ".join(self.get_dias()),
            "Desde: ": self.get_hora_inicio(),
            "Hasta: ": self.get_hora_fin()
        }
        json_response = json.dumps(response)
        return json_response
    # endregion
