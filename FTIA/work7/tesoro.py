"""
Implementación del entorno de la caza del tesoro para su resolución mediante programación
dinámica.

La clase incluye: una malla cuadrada con obstáculos
 y posiciones finales que pueden ser trampas o tesoros. Los estados son tuplas (fila,
 columna). Los movimientos (acciones) son estocásticos y de cuatro vecinos y se representan por
 números:  0 - arriba; 1 - derecha; 2 - abajo; 3 - izquierda. El efecto es desplazarse en la
 dirección indicada o en las sucesivas 3 en sentido horario según la distribución de
 probabilidades indicada por el array 'modelo'.

Moverse a una posición obstáculo o fuera de la malla deja la posición invariable.

Para cada transición, la recompensa es la asociada al estado de partida. Cualquier acción
en un estado final recibe la recompensa y termina el proceso. Las acciones en un proceso
terminado no tienen ningún efecto.

Incluye un método que genera una instancia del entrono correspondiente al ejemplo de
 la caza del tesoro de Russell y Norvig (aunque con coordenadas en notación fila/columna,
 en lugar de x/y).

La representación de obstáculos, finales y recompensas podría ser más compacta, al ser
matrices dispersas...¿te atreves?

nov/2019, nov/2020, nov/2021
L. Mandow
"""

from importlib import reload
import numpy as np
import sys
sys.path.append('.')

class Tesoro:
    """
    Entorno que representa el problema de la caza del tesoro (una malla con obstáculos,
     tesoros y trampas), donde los movimientos a los 4 vecinos tienen una componente
     estocástica definida por la lista 'modelo'.
    """

    # incremento en filas y columnas si queremos movernos en las cuatro direcciones
    # Direcciones: 0 - arriba; 1 - derecha; 2 - abajo; 3 - izquierda
    delta_f = np.array([-1, 0, 1,  0])
    delta_c = np.array([ 0, 1, 0, -1])

    def __init__(self, obstaculos, recompensas, finales, 
                 modelo = [0.8, 0.1, 0, 0.1]):
        """
        Los arrays obstaculos, recompensas y finales deben tener todos las mismas
        dimensiones, y cada posición representa un estado (salvo las indicadas como
        obstaculos).

        :param: obstaculos - array 2D que representa el entorno (0 - libre, 1- obstaculo)
        :param: recompensas - array 2D que representa el entorno con la recompensa de cada estado
        :param: finales - array 2D que representa el entorno (0 - normal, 1 - posicion final)
        :param: modelo - modelo probabilístico de transición, concretamente una lista con las
                         probabilidades de deslpazarnos realmente en cada dirección si la
                         acción es dir :[dir, dir+90º, dir+180º, dir+270º]
        """

        if not(obstaculos.shape == recompensas.shape == finales.shape):
            raise ValueError("Las matrices obstaculos, recompensas y finales no son del mismo tamaño.")

        if len(modelo) != 4:
            raise ValueError('El modelo no contempla exáctamente 4 acciones')

        self.obstaculos = obstaculos
        self.recompensas = recompensas
        self.finales = finales

        self.modelo = modelo             # distribución de probabilidad
        self.action_space = len(modelo)  # número de acciones

    def shape(self):
        return self.obstaculos.shape

    def recompensa(self, f,c):
        """
        :return: recompensa asociada al estado (f,c)
        """
        return self.recompensas[f,c]

    def pos_valida(self, f, c):
        """
        :return: True si la posición (f,c) está en los límites de la malla y no es un obstáculo
        """
        maxf, maxc = self.obstaculos.shape
        return ((0 <= f < maxf) and (0 <= c < maxc) and (self.obstaculos[f, c] != 1))

    def _deltas(self, f, c, d):
        """
        :return: incrementos de fila y columna si desde el estado (f,c) nos movemos REALMENTE en dirección d.
        Se tiene en cuenta que se rebota si se choca con los obstáculos o los límites de la malla.
        """
        df = self.delta_f[d]
        dc = self.delta_c[d]

        if self.pos_valida(f + df, c + dc):
            return df, dc
        else:
            return 0, 0

    def sucesores(self, f, c, d):
        """
        :return: dos valores: a) una lista con los cuatro sucesores de cada estado al realizar la
        accion d (puede haber repetidos si hay rebotes); b) secuencia con la probabilidad asociada
        a cada una de esas cuatro transiciones. Los estados sucesores se representan mediante tuplas.
        """
        sucesores = list()
        if (self.obstaculos[f, c] == 1) or (self.finales[f, c] == 1):
            return sucesores, list()

        for a in range(self.action_space):
            df, dc = self._deltas(f, c, int((d + a) % self.action_space))
            sucesores.append((f + df, c + dc))
        return sucesores, np.copy(self.modelo)

    def ver(self):
        print('OBSTÁCULOS:')
        print(self.obstaculos)

        print('RECOMPENSAS:')
        print(self.recompensas)

        print('FINALES:')
        print(self.finales)

        print('MODELO:')
        print(self.modelo)


#####################################################

def tesoro_rn():
    """
    Construye las matrices de obstaculos, recompensas y finales (que definen
    los estados) y el modelo de transición del problema de 'la caza del tesoro'
    de Russell y Norvig, y devuelve una instancia de Tesoro para ese problema.
    """

    obstaculos = np.array([[0, 0, 0, 0],
                           [0, 1, 0, 0],
                           [0, 0, 0, 0]])
    
    recompensas = np.ones((3,4))
    recompensas = recompensas * -0.04
    recompensas[1,1] = 0
    recompensas[0,3] = 1
    recompensas[1,3] = -1
    
    finales = np.array([[0, 0, 0, 1],
                        [0, 0, 0, 1],
                        [0, 0, 0, 0]])
    
    modelo = [0.8, 0.1, 0, 0.1]
    
    return Tesoro(obstaculos=obstaculos, recompensas=recompensas, finales=finales, modelo=modelo)


if __name__ == '__main__':
    #ejemplo
    entorno = tesoro_rn()
    entorno.ver()
