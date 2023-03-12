from Categoria import Categoria
from Categoria import categorias
class Peliculas(Categoria) :
    pelicula1 = 'john wick'
    pelicula2 = 'The Hangover'
    pelicula3 = 'scream'
    
    def generoPelicula() :
        return 'la pelicula {} es del genero {}'.format(n_pelicula.pelicula1, categorias.genero1)
    
n_pelicula = Peliculas 
print(n_pelicula.generoPelicula())