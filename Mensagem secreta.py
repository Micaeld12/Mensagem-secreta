import os
def renomear_arquivos():
    # Encontrar o nome dos arquivos na pasta
    lista_arquivos = os.listdir(r"/home/micael/Área de Trabalho/imagens")
    #print(lista_arquivos)
    diretorio_salvo = os.getcwd()
    print("O diretorio salvo foi "+diretorio_salvo)
    os.chdir(r"/home/micael/Área de Trabalho/imagens")
    # Renomear os arquivos da pasta
    for nome_arquivos in lista_arquivos:
        os.rename(nome_arquivos,nome_arquivos.translate(None, "0123456789"))
    os.chdir(diretorio_salvo)
renomear_arquivos()