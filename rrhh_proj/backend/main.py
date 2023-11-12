from models.actividades import Actividades
from models.lista_actividades import ListaActividades
from models.lista_horario import ListaHorario
from models.lugar_trabajo import LugarTrabajo
from models.horario import Horario
"""from models.cargo import Cargo
from models.divisa import Divisa
"""


def main():
    try:
        # Create instances of the needed classes

        # region Actividades
        # Creating an instance of it from a data string
        activ1_data_string = "Tarea1: Alto"
        actividad1 = Actividades.create_from_string(activ1_data_string)
        print(f"Region Actividades\nProbando con {actividad1.get_nombre()}\n" +
              f"Name:{actividad1.get_nombre()}\n" +
              f"Level:{actividad1.get_nivel()}\n")

        # Display the instance data as a JSON string
        data_activ1_as_json = Actividades.show_data(actividad1)
        print(f"Actividad1" +
              f"\nData as JSON format of {actividad1.get_nombre()}\n" +
              f"{data_activ1_as_json}\n")

        # Change instance attributes
        actividad1.set_nombre("Tarea 2")
        actividad1.set_nivel("Otro")

        activ2_data_string = "Tarea 3: Algo"
        actividad2 = Actividades.create_from_string(activ2_data_string)

        # Datas of the updated activ1 instance with the second one
        print(f"\nModified data as {actividad1.get_nombre()}\n" +
              f"Name:{actividad1.get_nombre()}\n" +
              f"Level:{actividad1.get_nivel()}\n" +
              f"\nActividad2\n" +
              f"Name:{actividad2.get_nombre()}\n" +
              f"Level:{actividad2.get_nivel()}\n")

        activ3_data_string = "Tarea 4: Bajo"
        actividad3 = Actividades.create_from_string(activ3_data_string)

        activ4_data_string = "Tarea 5: Medio"
        actividad4 = Actividades.create_from_string(activ4_data_string)

        activ5_data_string = "Tarea 6: Alto"
        actividad5 = Actividades.create_from_string(activ5_data_string)
        # endregion

        # region Lista Actividades
        # Creating an instance of it
        lista_activs = ListaActividades()

        # Adding Actividades
        lista_activs.add_actividad(
            actividad1, actividad2, actividad3, actividad4, actividad5)

        # Showing datas of the list
        data_activs_as_json = lista_activs.show_data()
        print(f"Region Lista Actividades\nData as JSON format of ListaActividades\n" +
              f"{data_activs_as_json}")

        # Updating
        print(f"\nUpdating {actividad4.get_nombre()}")
        # new_act=actividad2.set_nivel("Alto")
        lista_activs.update_actividad("Tarea 5", "Bajo")
        data_activs_as_json = lista_activs.show_data()
        print(f"Data as JSON format of ListaActividades\n" +
              f"{data_activs_as_json}")

        # Deleting Actividades from de collection
        print(
            f"\nDeleting {actividad5.get_nombre()},{actividad2.get_nombre()} from the collection")
        lista_activs.remove_actividades(actividad5, actividad2)

        data_activs_as_json = lista_activs.show_data()
        print(f"\nData as JSON format of ListaActividades\n" +
              f"{data_activs_as_json}\n")
        # endregion

        # region LugarTrabajo
        # Creating an instance of it from a data string
        lugar_trabajo1_data_string = "Proinso S.A,Sede Central,Asuncion,Avd. Sacramento c/ Profesor Mario Mariotti"
        lugar_trabajo1 = LugarTrabajo.create_from_string(
            lugar_trabajo1_data_string)
        print(f"Region Lugar Trabajo\nProbando con {lugar_trabajo1.get_nombre_empresa()}\n" +
              f"Name:{lugar_trabajo1.get_nombre_empresa()}\n" +
              f"Headquarter:{lugar_trabajo1.get_sucursal()}\n" +
              f"City:{lugar_trabajo1.get_ciudad()}\n" +
              f"Address:{lugar_trabajo1.get_ubicacion()}\n")

        # Display the instance data as a JSON string
        data_lugar_trab1_as_json = LugarTrabajo.show_data(lugar_trabajo1)
        print(f"Lugar Trabajo 1" +
              f"\nData as JSON format of {lugar_trabajo1.get_nombre_empresa()}\n" +
              f"{data_lugar_trab1_as_json}\n")

        # Change instance attributes
        lugar_trabajo1.set_nombre_empresa("Quattro Inversiones SA")
        lugar_trabajo1.set_ubicacion("Avd. España c/ Tte Alberto Román")
        lugar_trabajo1.set_ciudad("Asuncion")
        lugar_trabajo1.set_sucursal("Edificio España")

        lugar_trabajo2_data_string = "Origo Chocolate,Sede Central,Capital Federal,Edificio Alto Palermo"
        lugar_trabajo2 = LugarTrabajo.create_from_string(
            lugar_trabajo2_data_string)

        # Datas of the updated lugar_trabajo1 instance with the second one
        print(f"\nModified data as {lugar_trabajo1.get_nombre_empresa()}\n" +
              f"Name:{lugar_trabajo1.get_nombre_empresa()}\n" +
              f"Headquarter:{lugar_trabajo1.get_sucursal()}\n" +
              f"City:{lugar_trabajo1.get_ciudad()}\n" +
              f"Address:{lugar_trabajo1.get_ubicacion()}\n"
              f"\nLugar Trabajo 2\n" +
              f"Name:{lugar_trabajo2.get_nombre_empresa()}\n" +
              f"Headquarter:{lugar_trabajo2.get_sucursal()}\n" +
              f"City:{lugar_trabajo2.get_ciudad()}\n" +
              f"Address:{lugar_trabajo2.get_ubicacion()}\n")

        lugar_trabajo3_data_string = "Club Comodin SA,Mcal. Lopez y Avd. San Martin,Asuncion,Edificio Mcal. Lopez"
        lugar_trabajo3 = LugarTrabajo.create_from_string(
            lugar_trabajo3_data_string)

        lugar_trabajo4_data_string = "Coseres SA,General Elizardo Aquin-Ruta vieja,Luque,Edificio Kemsa"
        lugar_trabajo4 = LugarTrabajo.create_from_string(
            lugar_trabajo4_data_string)

        lugar_trabajo5_data_string = "Ion Monitor,Avd Molas Lopez,Asuncion,Edificio Plaza Real"
        lugar_trabajo5 = LugarTrabajo.create_from_string(
            lugar_trabajo5_data_string)
        # endregion

        # region Horario
        horario1_data_string = "Domingo,Lunes,Martes,Otro,Jueves,Viernes,Sabado,Domingo,19:00,22:00"
        horario1 = Horario.create_from_string(horario1_data_string)
        print(f"Region Horario \nProbando con {horario1.get_dias()}\n" +
              f"Dia/s:{horario1.get_dias()}\n" +
              f"Hora inicio:{horario1.get_hora_inicio()}\n" +
              f"Hora fin:{horario1.get_hora_fin()}\n")

        # Display the instance data as a JSON string
        data_horario1_as_json = Horario.show_data(horario1)
        print(f"Horario 1" +
              f"\nData as JSON format of {horario1.get_dias()}\n" +
              f"{data_horario1_as_json}\n")

        # Change instance attributes
        horario1.set_dias("Lunes, Sabado, Domingi, Lunes")
        horario1.set_hora_inicio("08:00")
        horario1.set_hora_fin("18:00")

        horario2_data_string = " Martes,11:11,04:18"
        horario2 = Horario.create_from_string(horario2_data_string)

        # Datas of the updated lugar_trabajo1 instance with the second one
        print(f"\nModified data as {horario1.get_dias()}\n" +
              f"Dia/s:{horario1.get_dias()}\n" +
              f"Hora inicio:{horario1.get_hora_inicio()}\n" +
              f"Hora fin:{horario1.get_hora_fin()}\n"
              f"\nHorario 2\n" +
              f"Dia/s:{horario2.get_dias()}\n" +
              f"Hora inicio:{horario2.get_hora_inicio()}\n" +
              f"Hora fin:{horario2.get_hora_fin()}\n")

        horario3_data_string = "Jueves,Viernes,Domingo,13:00,180:00"
        horario3 = Horario.create_from_string(horario3_data_string)

        horario4_data_string = "Viernes,Sabado,Domingo,08,15;00"
        horario4 = Horario.create_from_string(horario4_data_string)

        horario5_data_string = "Sabado,Domingo,23:00,21:59"
        horario5 = Horario.create_from_string(horario5_data_string)
        # endregion

        # region ListaHorario
        # Creating an instance of it
        lista_horarios = ListaHorario()

        # Adding Actividades
        lista_horarios.add_horario_lugar_trabajo(
            lugar_trabajo3, [horario2, horario1, horario5])

        # Showing datas of the list
        data_horarios_as_json = lista_horarios.show_data()
        print(f"\nRegion Lista Horarios\nData as JSON format of ListaHorarios\n" +
              f"{data_horarios_as_json}")

        # Updating the list
        print(
            f"\nUpdating {lugar_trabajo3.get_nombre_empresa()} and {horario1.get_dias()}")
        lugar_trabajo3.set_nombre_empresa("Mbokaja SA")
        new_horario1_data_string = horario1.set_hora_inicio(
            "12:00").set_hora_fin("22:00")
        new_horario1 = Horario()
        new_horario1.update_from_string(new_horario1_data_string)
        lista_horarios.update_horario_lugar_trabajo(
            lugar_trabajo3, [new_horario1])

        # endregion

    except ValueError as e:
        print(f"Error: {e}")


"""
The entry point of the script that is executed only when the script is executed directly, 
and not when it is imported as a module.
"""
if __name__ == "__main__":
    main()