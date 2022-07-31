import operacoes
from operacoes import *
from titulo import *
"""_summary_
CALCULADORA SIMPLES QUE FIZ PARA PRATICAR E EVOLUIR NESSE MEU INÍCIO EM PYTHON!!!

"""
cabecalho('CALCULADORA')

while True:
    print(linha())
    print('  1 - \033[1;32mADIÇÃO\033[m | 2 - \033[1;33mSUBTRAÇÃO\033[m | 3 - \033[1;34mMULTIPLICAÇÃO\033[m | 4 - \033[1;95mDIVISÃO\033[m\n  5 - \033[1;31mSAIR\033[m')
    print(linha())
    resposta = leiaInt('\033[1;36mRESPOSTA:\033[m ')
    
    if resposta == 1: 
        cabecalho('ADIÇÃO')   
        Calculadora.adicao()
    elif resposta == 2:
        cabecalho('SUBTRAÇÃO')
        Calculadora.subitracao()
    elif resposta == 3:
        cabecalho('MULTIPLICAÇÃO')
        Calculadora.multiplicacao()
    elif resposta == 4:
        cabecalho('DIVISÃO')
        divide = Calculadora.divisao()
    elif resposta == 5:
        print(linha())
        print(f'\033[1;92mVolte Sempre!!!\033[m'.rjust(74))
        break  
        
                   