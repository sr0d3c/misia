# -*- coding: utf-8 -*- 
"""
Created on Nov 2019, Nov 2020, Nov 2021
@author: Lawrence Mandow

Agente para resolver mediante programación dinámica problemas en entornos como
el descrito en tesoro21base.py. Concretamente se emplea iteración de políticas.

Se supone que el entorno tiene una interfaz con los métodos:
shape()
pos_valida(f,c)
recompensa(f,c)
sucesores(f,c)

y la propiedad:
action_space
"""

from importlib import reload
import matplotlib.pyplot as plt
from tesoro import *

class AgentePD:
    def __init__(self, entorno: Tesoro, gamma: float = 1.0):
        """
        :param: entorno - instancia de un entorno que cumpla la misma interfaz de la clase Tesoro21
        (propiedad action_space y métodos shape(), sucesores(f,c,d), recompensa(f,c) y pos_valida (f,c).
        :param: gamma - tasa de descuento en el intervalo (0, 1]
        """

        self.entorno = entorno
        self.gamma = gamma
        
        #representación interna de la función de valor (v) y la política
        self.politica = np.zeros(self.entorno.shape())
        self.v = np.zeros(self.entorno.shape())

        #valor inicial para pruebas
        # self.v = np.array([[0.812, 0.868, 0.918, 1.0],
        #                    [0.762, 0, 0.660, -1.0],
        #                    [0.705, 0.655, 0.611, 0.388]])

        #valor inicial para pruebas
        # self.politica = np.array([[1, 1, 1, 0],
        #                           [0, 0, 0, 0],
        #                           [0, 3, 3, 3]])

    def ver(self):
        self.ver_politica()
        self.ver_v()

    def ver_politica(self):
        print('Política:')
        print(str(self.politica))

    def ver_v(self):
        print('Valores:')
        print(str(self.v))

    def valor(self, f, c, d):
        """
        Valor esperado de la acción d en el estado (f,c)
        """
        r = self.entorno.recompensa(f, c)

        suma = 0
        for s2, p in zip(*self.entorno.sucesores(f,c,d)):
            fn = s2[0]
            cn = s2[1]
            suma += p * self.v[fn, cn]

        return r + self.gamma * suma


    def evaluacion(self,it = 1000):
        """
        evaluación de la política actual con it iteraciones
        """
        #self.v = np.zeros(self.entorno.shape())
        nf, nc = self.v.shape
        for i in range(it):
            v2 = self.v.copy()
            for f in range(nf):
                for c in range(nc):
                    if(self.entorno.pos_valida(f, c)):
                        v2[f, c] = self.valor(f, c, self.politica[f, c])
            self.v = v2

    def mejora(self):
        """
        Mejora la política actual usando los valores de self.v
        """
        nf, nc = self.politica.shape
        for f in range(nf):
            for c in range(nc):
                valores = []
                for a in range(self.entorno.action_space):  # las 4 direcciones
                   valores.append(self.valor(f, c, a))
                amax = np.argmax(np.array(valores))  # indice de la mejor acción
                self.politica[f, c] = amax

    def calcula_politica_optima(self, it_evaluacion =1000 , it=20, eco=True):
        """
        Alterna evaluación y mejora hasta que la política no cambia
        it_evaluacion indica cuántas iteraciones se realizarán de evaluacion
        cada vez.
        """
        iguales = False
        while not (iguales) or it > 0:
            it = it - 1
            p2 = self.politica.copy()
            self.evaluacion(it_evaluacion)
            self.mejora()

            iguales = np.array_equal(self.politica, p2)

            if eco:
                self.ver_v()
                self.ver_politica()



if __name__ == '__main__':
    
    #elementos que definen el entorno de 'la caza del tesoro'
    ent = tesoro_rn()

    #Creamos un agente para 'la caza del tesoro'
    ag = AgentePD(ent, gamma=1.0)
    #ag.evaluacion()
    #ag.mejora()
    ag.calcula_politica_optima(it_evaluacion=1, it=15)

    ag.ver_politica()
    ag.ver_v()
