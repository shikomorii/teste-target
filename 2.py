import math


def verificaco(Numero):
    raiz = int(math.sqrt(Numero))
    return raiz * raiz == Numero

def fibonaci(n):
    cond1 = 5 * n * n + 4
    cond2 = 5 * n * n - 4

  
    if verificaco(cond1) or verificaco(cond2):
        return True
    else:
        return False


numero = int(input("Digite um número: "))


if fibonaci(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")
