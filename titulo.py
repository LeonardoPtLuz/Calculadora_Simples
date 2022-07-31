def linha(tam = 64):
    return '=' * tam


def cabecalho(txt):
    print(linha())
    print(f'{txt:^64}')
    print(linha())