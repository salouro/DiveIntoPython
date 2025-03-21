import re

class LazyRules:
    """
        Carrega as regras de pluralidade de forma "preguiçosa". 
    """
    #Constante que define o nome do arquivo
    rules_filename = './ClassesIterators/plural6-rules.txt'   

    def __init__(self):
        self.pattern_file = open(self.rules_filename, encoding='utf-8')
        self.cache = []

    #Inicia o iterador e configura o indice do cache como 0
    def __iter__(self):
        self.cache_index = 0
        return self
    
    def __next__(self):
        self.cache_index += 1
        #Se já estiver cacheado, retorna do cache
        if len(self.cache) >= self.cache_index:
            return self.cache[self.cache_index - 1]
        
        #Se acabou o arquivo, para a iteração
        if self.pattern_file.closed:
            raise StopIteration
        
        line = self.pattern_file.readline()
        if not line:
            self.pattern_file.close()
            raise StopIteration
        
        pattern, search, replace = line.split(None, 3)
        funcs =  self.build_match_and_apply_functions(pattern, search, replace)
        self.cache.append(funcs)        
        return funcs
    
    def build_match_and_apply_functions(self, pattern, search, replace):
        def match_rule(word):
            return re.search(pattern, word)
        def apply_rule(word):
            return re.sub(search, replace, word)
        return (match_rule, apply_rule)
    

