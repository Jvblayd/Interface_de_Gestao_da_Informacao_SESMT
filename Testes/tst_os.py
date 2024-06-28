import os

diretorio_atual = os.getcwd()

palav = 'simbora'

try:
    open(f'{diretorio_atual}\\zados.txt','x')

    with open(f'{diretorio_atual}\\zados.txt','r') as leitura:
        linha = leitura.readline()

    with open(f'{diretorio_atual}\\zados.txt','w') as escrita:
        if len(linha) == 0:
            escrita.write(palav)
        else:
            escrita.write(f'{linha};{palav}')

except FileExistsError:
    with open(f'{diretorio_atual}\\zados.txt','r') as leitura:
        linha = leitura.readline()

    with open(f'{diretorio_atual}\\zados.txt','w') as escrita:
        if len(linha) == 0:
            escrita.write(palav)
        else:
            escrita.write(f'{linha};{palav}')
    