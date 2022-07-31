def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except(ValueError, TypeError):
            print('\033[1;31mERRO: Valor inserido não é válido!\033[m')
        else:
            return num


def leiaReal(msg):
    while True:
        try:
            num = float(input(msg))
        except(ValueError, TypeError):
            print('\033[1;31mERRO: Valor inserido não é válido!\033[m')
        else:
            return num

            
class Calculadora:
    def adicao():
        num1 = leiaReal('Adição: ')
        num2 = leiaReal('Adição: ') 
        soma = num1 + num2 
        print(f'\033[1;32mResposta: {soma}\033[m')
        return soma


    def subitracao():
        num1 = leiaReal('¹Subtração: ')        
        num2 = leiaReal('²Subtração: ')
        subtrai = num1 - num2
        print(f'\033[1;33mResposta: {subtrai}\033[m')
        return subtrai


    def multiplicacao():
        num1 = leiaReal('¹Multiplicação: ')
        num2 = leiaReal('²Multiplicação: ')
        multiplica = num1 * num2
        print(f'\033[1;34mResposta: {multiplica}\033[m')
        return multiplica


    def divisao():
        num1 = leiaReal('¹Divisão: ')
        num2 = leiaReal('²Divisão: ')
        divide = num1 / num2
        print(f'\033[1;95mResposta: {divide}\033[m')
        return divide