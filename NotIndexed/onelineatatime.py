#Abre um arquivo e imprime suas linhas uma-a-uma
line_number = 0
#Se encoding não for especificado, abre o arquivo no encoding padrão para o os (locale.getpreferredencoding())
with open('C:/Users/felipe.a/default-soapui-workspace.xml', encoding='utf-8') as a_file:
    #Um stream de bytes é um iterator
    for a_line in a_file:
        line_number += 1
        #formata a linha 
        print('{:>4} {}'.format(line_number, a_line.rstrip()))
