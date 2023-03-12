from Jugador1 import Jugador1
from Jugador2 import Jugador2
from Jugador1 import n_jugador1
from Jugador2 import n_jugador2
class Juego(Jugador1,Jugador2) :
    def __init__(self, coin):
        self.coin = coin
        #coin decidira quien empieza
    def darseRiatasos(self) :
        if nuevo_juego.coin == 'cara':
            print( n_jugador1.luchador + ' inicia con el primer golpe')
            n_jugador2.vida = n_jugador2.vida-n_jugador1.atk
            print('la vida de '+ n_jugador2.luchador +'  bajo a ', n_jugador2.vida, ', ahora se prepara para contra atacar')
            n_jugador1.vida = n_jugador1.vida-n_jugador2.atk
            print('la vida de '+ n_jugador1.luchador +'  bajo a ', n_jugador1.vida, ', ahora se prepara para contra atacar')
            n_jugador1.atk = 500
            n_jugador2.vida = n_jugador2.vida-n_jugador1.atk
            print('la vida de '+ n_jugador2.luchador +'  bajo a ', n_jugador2.vida, ', el luchador ', Jugador1.luchador, 'saco un poder del qlo dandole', Jugador1.atk , ' de daño y asi obteniendo la victoria')
nuevo_juego = Juego('cara')


print(n_jugador1.jugador1Informacion())
print(n_jugador2.jugador2Informacion())
print(nuevo_juego.darseRiatasos())