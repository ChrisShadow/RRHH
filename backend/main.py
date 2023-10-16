from models.actividades import Actividades
from models.lista_actividades import ListaActividades
"""from models.cargo import Cargo
from models.divisa import Divisa
from models.horario import Horario
from models.lista_horario import LugarTrabajo"""

def main():
    try:
        # Create instances of the needed classes

        #Actividades: Creating an instance of it from a data string
        activ1_data_string="Tarea1: Mala"
        actividad1=Actividades.create_from_string(activ1_data_string)
            
        # Display the instance data as a JSON string
        data_activ1_as_json=Actividades.show_data(actividad1)
        print(f"Actividad1"+
              f"\nData as JSON format of {actividad1.get_nombre()}\n"+
            f"{data_activ1_as_json}")

        # Change instance attributes
        actividad1.set_nombre("Tarea 2")
        actividad1.set_nivel("Alto")

        activ2_data_string="Tarea 3: Buena"
        actividad2=Actividades.create_from_string(activ2_data_string)
        
            
        #Datas of the updated activ1 instance with the second one
        print(f"Modified data as {actividad1.get_nombre()}\n"+
            f"Name:{actividad1.get_nombre()}\n"+
            f"Level:{actividad1.get_nivel()}\n"+
            f"\nActividad2\n"+
            f"Name:{actividad2.get_nombre()}\n"+
            f"Level:{actividad2.get_nivel()}\n")
        
        activ3_data_string="Tarea 4: Bajo"
        actividad3=Actividades.create_from_string(activ3_data_string)

        activ4_data_string="Tarea 5: Medio"
        actividad4=Actividades.create_from_string(activ4_data_string)

        activ5_data_string="Tarea 6: Alto"
        actividad5=Actividades.create_from_string(activ5_data_string)
        
        #Lista Actividades: Creating an instance of it
        lista_activs=ListaActividades()

        #Adding Actividades
        lista_activs.add_actividad(actividad1,actividad2,actividad3,actividad4,actividad5)

        #Showing datas of the list
        data_activs_as_json=lista_activs.show_data()
        print(f"Data as JSON format of ListaActividades\n"+
            f"{data_activs_as_json}")
    except ValueError as e:
         print(f"Error: {e}")

"""
The entry point of the script that is executed only when the script is executed directly, 
and not when it is imported as a module.
"""
if __name__=="__main__":
    main()