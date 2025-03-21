import locale

arquivos = ('teste.log', 'outroTeste.log', 'maisUmTeste.log')
encoding = locale.getpreferredencoding()

for arquivo in arquivos:
    #Cria e escreve um arquivo. Função open() já cria um arquivo se o mesmo não existir. Modo "w" sobrescreve qualquer conteúdo do arquivo.
    with open(arquivo, mode='w', encoding = encoding) as a_file:
        #Escreve no arquivo
        a_file.write(F"Teste bem-sucedido, o nome desse arquivo é {arquivo}")

    with open(arquivo) as a_file:
        print(a_file.read())

    #Modo "a" adiciona ao final do arquivo
    with open(arquivo, mode='a', encoding = encoding) as a_file:
        a_file.write("E de novo")

    with open(arquivo, mode='r', encoding = encoding) as a_file:
        print(a_file.read())


