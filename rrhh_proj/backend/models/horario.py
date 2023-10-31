import json
import re

class Horario():

    # region constructor
    def __init__(self, dias, hora_inicio, hora_fin):
        self.dias = dias
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
    # endregion

    # region getter
    def get_dias(self):
        return self.dias

    def get_hora_inicio(self):
        return self.hora_inicio

    def get_hora_fin(self):
        return self.hora_fin
    # endregion

    # region setter
    def set_dias(self, new_days_string):
        """accepts a list of days and checks if all days entered are valid. 
        If they are all valid, it updates the value of the _days attribute, and if they are not, 
        it generates a ValueError."""
        #Valid only days list
        dias_posibles = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
        
        # Divides the string into days using commas as separators
        new_days = new_days_string.split(",")
        #Remove duplicates and validate days
        unique_dias = []  # List to store unique days
        duplicate_dias = []  # List to store duplicated days
        invalid_dias = []  # List to store invalid days
        
        for dia in new_days:
            dia_stripped = dia.strip()

            if dia_stripped in unique_dias:
                # Duplicate day found, we add it to the list of duplicates.
                duplicate_dias.append(dia_stripped)
            elif dia_stripped in dias_posibles:
                unique_dias.append(dia_stripped)  # We add only if it is a valid day
            else:
                # Invalid day found, we add it to the invalid list.
                invalid_dias.append(dia_stripped)

        if duplicate_dias:
            print(f"Días duplicados eliminados: {', '.join(duplicate_dias)}")
    
        if invalid_dias:
            print(f"Día(s) no válido(s) encontrados: {', '.join(invalid_dias)}")

        if not unique_dias:
            # If there are no valid single days, set "Monday" as the default day.
            unique_dias = ["Lunes(default)"]

        self.dias=unique_dias

    def set_hora_inicio(self, new_starting_hour):
        # Defines a regular expression pattern to validate the time format
        hora_patron = r"^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$"

        if re.match(hora_patron, new_starting_hour):
            self.hora_inicio = new_starting_hour
        else:
            #raise ValueError("El formato de la hora no es válido. Debe ser ##:##.")
            print("El formato de la hora no es válido. Debe ser ##:##.")
            self.hora_inicio='08:00(Default)'

    def set_hora_fin(self, new_leaving_hour):
        # Defines a regular expression pattern to validate the time format
        hora_patron = r"^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$"

        if re.match(hora_patron, new_leaving_hour):
            self.hora_fin = new_leaving_hour
        else:
            #raise ValueError("El formato de la hora no es válido. Debe ser ##:##.")
            print("El formato de la hora no es válido. Debe ser ##:##.")
            self.hora_fin='17:00(Default)'

    # endregion

    # region methods
    @classmethod
    def create_from_string(cls, data_string):
        """dias, hora_inicio, hora_fin = map(str.strip,data_string.lstrip().split(","))
            
        if dias.lstrip() not in ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']:
            #raise ValueError("Día(s) inválido(s)")
            print("Día(s) inválido(s)")
            dias='Lunes(Default)'"""
        
        #Dividing the chain into parts
        parts=data_string.split(',')

        #Extract the values
        dias=parts[:-2] #Get a list of days (all but the last two)
        hora_inicio=parts[-2]
        hora_fin=parts[-1]

        #Validate the days
        dias_posibles = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

        #Remove duplicates and validate days
        unique_dias = []  # List to store unique days
        duplicate_dias = []  # List to store duplicated days
        invalid_dias = []  # List to store invalid days
        for dia in dias:
            dia_stripped = dia.strip()
            if dia_stripped in unique_dias:
                # Duplicate day found, we add it to the list of duplicates.
                duplicate_dias.append(dia_stripped)
            elif dia_stripped in dias_posibles:
                unique_dias.append(dia_stripped)  # We add only if it is a valid day
            else:
                # Invalid day found, we add it to the invalid list.
                invalid_dias.append(dia_stripped)

        if duplicate_dias:
            print(f"Días duplicados eliminados: {', '.join(duplicate_dias)}")
    
        if invalid_dias:
            print(f"Día(s) no válido(s) encontrados: {', '.join(invalid_dias)}")

        if not unique_dias:
            # If there are no valid single days, set "Monday" as the default day.
            unique_dias = ["Lunes(default)"]
        
        # Defines a regular expression pattern to validate the time format
        hora_patron = r"^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$"

        if not re.match(hora_patron, hora_inicio):
            #raise ValueError("El formato de la hora no es válido. Debe ser ##:##.")
            print("El formato de la hora no es válido. Debe ser ##:##.")
            hora_inicio='08:00(Default)'

        if not re.match(hora_patron, hora_fin):
            #raise ValueError("El formato de la hora no es válido. Debe ser ##:##.")
            print("El formato de la hora no es válido. Debe ser ##:##.")
            hora_fin='17:00(Default)'

        #Create an instance and assign the values
        horario = cls(unique_dias, hora_inicio.strip(), hora_fin.strip())

        return horario

    #@classmethod
    def show_data(self): #horario
        #days = horario.get_dias()
        #days_combined = ", ".join(days)  # Joining days with a comma and a space
        response = {
            "Dias: ": ", ".join(self.get_dias()) ,
            "Desde: ": self.get_hora_inicio(),
            "Hasta: ": self.get_hora_fin()
        }
        json_response = json.dumps(response)
        return json_response
    # endregion