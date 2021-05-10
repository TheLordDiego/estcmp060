# Árvore Y Fractal em Python usando Turtle
# Codificado seguindo as boas práticas do PEP8

from turtle import *

speed('fastest')

# girando a tartaruga para cima
rt(-90)

# o ângulo agudo entre
# a base e o ramo do --Y--
angulo = 30

# função para desenhar um --Y--
def y(sz, nivel):
    if nivel > 0:
        colormode(255)

        # divisão do intervalo rgb para verde
        # em intervalos iguais para cada nível
        # definindo a cor de acordo ao nível atual
        pencolor(0, 255 // nivel, 0)

        # desenhando a base
        fd(sz)

        rt(angulo)

        # chamada recursiva para a sub-árvore certa
        y(0.8 * sz, nivel - 1)

        pencolor(0, 255 // nivel, 0)

        lt(2 * angulo)

        # chamada recursiva para a subárvore esquerda
        y(0.8 * sz, nivel - 1)

        pencolor(0, 255 // nivel, 0)

        rt(angulo)
        fd(-sz)


# árvore de tamanho 80 e nível 7
y(80, 7)