# Fibonacci e fractal espiral usando o módulo Turtle
# Codificado seguindo as boas práticas do PEP8
import turtle
import math

def fibo_plot(n):
    a = 0
    b = 1
    quadrado_a = a
    quadrado_b = b

    # Definindo a cor da caneta para --azul--
    x.pencolor("blue")

    # Desenhando o primeiro quadrado
    x.forward(b * fator)
    x.left(90)
    x.forward(b * fator)
    x.left(90)
    x.forward(b * fator)
    x.left(90)
    x.forward(b * fator)

    # Processando a Série Fibonacci
    temp = quadrado_b
    quadrado_b = quadrado_b + quadrado_a
    quadrado_a = temp

    # Desenhando os outros quadrados
    for i in range(1, n):
        x.backward(quadrado_a * fator)
        x.right(90)
        x.forward(quadrado_b * fator)
        x.left(90)
        x.forward(quadrado_b * fator)
        x.left(90)
        x.forward(quadrado_b * fator)

        # Processando a Série Fibonacci
        temp = quadrado_b
        quadrado_b = quadrado_b + quadrado_a
        quadrado_a = temp

    # Colocando a caneta no ponto inicial do gráfico espiral
    x.penup()
    x.setposition(fator, 0)
    x.seth(0)
    x.pendown()

    # Definindo a cor da caneta para --vermelho--
    x.pencolor("red")

    # Desenhando a Espiral Fibonacci
    x.left(90)
    for i in range(n):
        print(b)
        fdwd = math.pi * b * fator / 2
        fdwd /= 90
        for j in range(90):
            x.forward(fdwd)
            x.left(1)
        temp = a
        a = b
        b = temp + b


# Variavel para fator multiplicativo que aumenta ou diminui
# conforme o contexto de execução
fator = 1

# Informa o número de iterações a ser executada
n = int(input('Informe o número de iterações desejada (deve ser > 1) : '))

# Traçando o Fractal Espiral de Fibonacci
# e imprimindo o Número Fibonacci correspondente
if n > 0:
    print("Série Fibonacci para ", n, "elementos :")
    x = turtle.Turtle()
    x.speed(100)
    fibo_plot(n)
    turtle.done()
else:
    print("O número de iterações deve ser > 0 ")
