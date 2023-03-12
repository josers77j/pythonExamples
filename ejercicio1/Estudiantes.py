from Materias import Materias

from Notas import Notas
from Notas import n_nota

class Estudiantes(Materias,Notas) :
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
#pude haber sido mas especifico en el resultado de la calificacion dandole el 60% al lab y el 40% al parcial, pero para efectos
#practicos, decidi hacerlo de esta forma.
    def mostrarCalificaciones(self) :
        return '{} con codigo {} saco la calificacion de {} en la materia {}'.format(self.nombre,self.codigo, (n_nota.lab+n_nota.parcial)/2, Materias.materia) 
        
n = Estudiantes('oscar','u20140507')

print(n.mostrarCalificaciones())
