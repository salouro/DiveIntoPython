import plural6

def plural(palavra, pluralizer : plural6.LazyRules):
    for regra in pluralizer:                     
        if regra[0](palavra):
            return regra[1](palavra)


def main():
    pluralizer = plural6.LazyRules()
    palavras = ("álbum", "rua", "casa", "amor")
    for palavra in palavras:
        print(plural(palavra, pluralizer))

main()