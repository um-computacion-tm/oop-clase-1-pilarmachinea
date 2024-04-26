
"""
- profe_elio tiene estado(sabe su nombre)
- En las clases cada objeto tiene su proria variable
- Podemos cambiar el nombrede gabi en la terminal pero al de elio no le va a pasar nada
- Si buscamos profe_gabi en la terminal nos va a dar que es profesor y un "codigo" que es donde esta guardado en la mamoria
- Los objetos tienen estado
- Para poder crear objeto necesito un constructor
- Self = yo mismo profeosr o alumno depende de donde este
- En la terminal cuando preguntas por inasistencias para agregar una += 1
- Tener la menor cantidad de estados posibles
- Estados calculados
"""

class Profesor:
    def __init__(self, el_nombre, el_email):
        self.__nombre__ = el_nombre
        self.__email__ = el_email

#metodo adentro de una clase, esto devuelve el nombre 
    def dame_tu_nombre(self):
        return self.__nombre__


class Alumno:
    def __init__(self, el_nombre_del_alumno):
        self.__nobmre__ = el_nombre_del_alumno
        self.__inasistencia__ = 0
        self.__dieta__ = ""
        self.__mentor__ = None

    def mentoria(self, profesor):
        self.__mentor__ = profesor  

    def falta(self):
        self.__inasistencia__ +=1

    def elegir_dieta_especial(self, la_dieta):
        self.__dieta__ =la_dieta 

    def es_vegano(self):
        self.__dieta__ = "vegano"

    def esta_libre(self):
        if self.__inasistencia__ >= 5:
            return "Esta libre"
        else:
            return "Ok"
#class es uno solo profesor/alumno 


profe_elio = Profesor("Elio", "elio@gmail.com")
profe_gabi = Profesor("Gabriel", "gabi@gmail.com")

print(profe_elio.dame_tu_nombre())
print(profe_gabi.dame_tu_nombre())
#no es una funcion

alumno_juan = Alumno("Juancito")
alumno_maria = Alumno("Maria")
#N profesores/alumnos

alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
print(alumno_juan.esta_libre())
alumno_juan.falta()
print(alumno_juan.esta_libre())
#Va a imprimir ambos resultados ya que falta 4 y 5 veces

los_alumnos = [alumno_juan, alumno_maria]

alumno_maria.elegir_dieta_especial("vegetariana")
print(alumno_maria.dieta)
alumno_juan.es_vegano()
print(alumno_juan.dieta)

alumno_juan.mentoria(profe_elio)
print(alumno_juan.mentor)

import ipdb; ipdb.set_trace()  
