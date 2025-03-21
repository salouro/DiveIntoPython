import sys

class RedirectStdoutTo:
    """Redireciona os outputs do sdtout. Classe como context manager."""

    #Inicialização da classe
    def __init__(self, out_new):
        self.out_new = out_new

    #Qualquer classe pode ser um context manager, basta ter dois métodos: __enter__ e __exit__
    def __enter__(self):
        #Cria uma variável e direciona o stdout para ela
        self.out_old = sys.stdout
        #Manipula o stdout
        sys.stdout = self.out_new

    def __exit__(self, *args):
        sys.stdout = self.out_old


print('A')

#Escreve no arquivo com PRINT
with open('C:/Projetos/Python/out.log', mode='w', encoding='utf-8') as a_file, RedirectStdoutTo(a_file):
    print('B')
          
print('C')
