from Peliculas import Peliculas
from Categoria import Categoria
from Categoria import categorias
class Clientes(Peliculas,Categoria) :
    pass
    def __init__(self, nombre, seleccion):
        self.nombre = nombre
        self.seleccion = seleccion
        
    def escogerPelicula(self) :
        if categorias.genero1 == n_cliente.seleccion : 
         return '{} ha elegido la categoria {} la pelicula con ese genero es {}'.format(self.nombre, categorias.genero1,Peliculas.pelicula1)
        elif categorias.genero2 == n_cliente.seleccion : 
         return '{} ha elegido la categoria {} la pelicula con ese genero es {}'.format(self.nombre, categorias.genero2,Peliculas.pelicula2)
        elif categorias.genero3 == n_cliente.seleccion : 
         return '{} ha elegido la categoria {} la pelicula con ese genero es {}'.format(self.nombre, categorias.genero3,Peliculas.pelicula3)
     

n_cliente = Clientes('raspery','accion')
        
print(n_cliente.escogerPelicula())