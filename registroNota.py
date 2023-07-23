from Alumnos import Alumno

if __name__ == '__main__':
    estudiantes = []
    comandosSistema = ['R', 'P', 'M', 'X', 'C', 'S']

    while True:
        comandoInformacion = input("Ingrese un comando: ")
        print(f"El comando ingresado es {comandoInformacion}")
        if comandoInformacion in comandosSistema:
            if comandoInformacion == 'R':
                print("Se registrará un nuevo estudiante:")
                nombre = input("Ingrese nombre del estudiante: ")
                apellido = input("Ingrese apellido del estudiante: ")
                edad = input("Ingrese edad del estudiante: ")
                nacionalidad = input("Ingrese nacionalidad del estudiante: ")
                objAlumno = Alumno(nombre, apellido, edad, '', nacionalidad)
                estudiantes.append(objAlumno)
            elif comandoInformacion == 'M':
                print("Se mostrará la información de los estudiantes:")
                i = 0
                for estudiante in estudiantes:
                    print(f"Información del estudiante {i}:")
                    print(f"Nombre del alumno: {estudiante.nombre}")
                    print(f"Apellido del alumno: {estudiante.apellido}")
                    print(f"Edad del alumno: {estudiante.edad}")
                    print(f"Nota del alumno: {estudiante.nota}")
                    print(f"Nacionalidad del alumno: {estudiante.nacionalidad}")
                    i += 1
                    print("\n")
            elif comandoInformacion == 'C':
                print("Se ingresarán las notas de los alumnos registrados:")
                for estudiante in estudiantes:
                    while True:
                        nota = input(f"Alumno {estudiante.nombre} {estudiante.apellido}, ingrese nota: ")
                        try:
                            nota_float = float(nota)
                            if estudiante.validarNota(nota_float):
                                if estudiante.registrarNota(nota_float):
                                    print("Nota registrada exitosamente.")
                                    break
                                else:
                                    print("Error al registrar la nota. Digite nuevamente.")
                            else:
                                print("La nota ingresada no es válida. Digite nuevamente.")
                        except ValueError:
                            print("Error: La entrada no es un número válido. Digite nuevamente.")
            elif comandoInformacion == 'P':
                print("Se calculará el promedio de notas de todos los alumnos registrados:")
                cantidad_alumnos = 0
                suma_notas = 0
                for estudiante in estudiantes:
                    cantidad_alumnos += 1
                    suma_notas += estudiante.leerNota()
                if cantidad_alumnos > 0:
                    promedio = suma_notas / cantidad_alumnos
                    print(f"El promedio de notas para {cantidad_alumnos} alumno(s) es: {promedio}")
                else:
                    print("No hay alumnos registrados.")
            elif comandoInformacion == 'S':
                print("Se mostrará la suma de notas de todos los alumnos registrados:")
                cantidad_alumnos = 0
                suma_notas = 0
                for estudiante in estudiantes:
                    cantidad_alumnos += 1
                    suma_notas += estudiante.leerNota()
                print(f"La suma de notas de {cantidad_alumnos} alumno(s) es: {suma_notas}")
            elif comandoInformacion == 'X':
                print("Comando de finalización")
                break
        else:
            print("Comando incorrecto. Digite nuevamente.")
