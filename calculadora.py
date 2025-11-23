# calculadora.py
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida!"
    return a / b

def potencia(base, expoente=2):
    return base ** expoente

def raiz_quadrada(num):
    if num < 0:
        return "Erro: Não é possível calcular raiz quadrada de número negativo!"
    return num ** 0.5

def mensagem_secreta():
    return "Eu odeio carro elétrico... mas amo Python! "

# Lista de operações disponíveis (útil para o main.py)
OPERACOES = {
    "1": ("Somar", somar),
    "2": ("Subtrair", subtrair),
    "3": ("Multiplicar", multiplicar),
    "4": ("Dividir", dividir),
    "5": ("Potência", potencia),
    "6": ("Raiz Quadrada", raiz_quadrada),
}