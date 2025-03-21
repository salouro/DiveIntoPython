import gzip

'''Demonstrando a capacidade do Python de lidar com arquivos comprimidos'''

#Cria o arquivo comprimido, todo arquivo comprimido deve ser aberto em modo BINÁRIO
with gzip.open('C:/Projetos/Python/out.log.rar', mode='wb') as arquivo_comprimido:
    arquivo_comprimido.write('Uma caminhada de 6 quilômetros nao é brincadeira, especialmente na chuva'.encode('utf-8'))
