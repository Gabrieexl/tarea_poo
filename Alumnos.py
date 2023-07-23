class Alumno:
    def __init__(self, nombre, apellido, edad, nota, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nota = nota
        self.nacionalidad = nacionalidad

    def leerNota(self):
        return self.nota

    def registrarNota(self, notaAlumno):
        if self.validarNota(notaAlumno):
            self.nota = notaAlumno
            return True
        else:
            return False

    def validarNota(self, nota):
        if isinstance(nota, (int, float)):
            return 0 <= nota <= 20
        else:
            return False
