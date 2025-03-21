#Classes seguem o padrão CamelCase
class Fib:
    """
    Iterator que devolve os números de uma sequência Fibonacci de acordo com max
    max:number -> Máximo número gerado pela sequência Fibonacci
    """

    #Construtor da classe
    def __init__(self, max):
        self.max = max

    #Inicia o iterator
    def __iter__(self):
        self.a = 0
        self.b = 1
        return self
    
    def __next__(self):
        fib = self.a
        if fib > self.max:
            #Para iteração
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib