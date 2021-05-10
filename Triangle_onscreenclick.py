# Triangulo em Python Turtle usando onscreenclick
# Codificado seguindo as boas práticas do PEP8

import turtle

# Método Screen () para obter a tela
wn = turtle.Screen()

# criando objeto tess
tess = turtle.Turtle()


def triangulo(x, y):
    # levantando a caneta
    tess.penup()

    # movendo o cursor nas posições --x-- e --y--
    tess.goto(x, y)

    # baixando a caneta (para desenhar)
    tess.pendown()
    for i in range(3):
        # movendo o cursor 100 unidades para frente
        tess.forward(100)

        # virando o cursor 120 graus para esquerda
        tess.left(120)

        # movendo o cursor 100 unidades para frente
        tess.forward(100)


# função especial embutida para enviar corrente
# a posição do cursor para o triângulo
turtle.onscreenclick(triangulo, 1)

turtle.listen()

# matendo a tela após execução
turtle.done()