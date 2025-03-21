import re

"""
def match_sxz(noun):
    return re.search('[sxz]$', noun)

def match_h(noun):
    return re.search('[^aeioudgkprt]h$', noun)

def apply_sxz_h(noun):
    return re.sub('$', 'es', noun)

def match_y(noun):
    return re.search('[^aeiou]y$', noun)

def apply_y(noun):
    return re.sub('y$', 'ies', noun)

def match_default(noun):
    return True

def apply_default(noun):
    return noun + 's'"""

"""
patterns = (
    ('[sxz]$',              '$',  'es'),
    ('[^aeioudgkprt]h$',    '$',  'es'),
    ('(qu|[^aeiou])y$',     'y$', 'ies'),
    ('$',                   '$',  's')
    )
    
rules = [build_match_and_apply_functions(pattern, search, replace)
         for (pattern, search, replace) in patterns]
"""

def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

rules = []
with open('C:/Projetos/Python/DiveIntoPython/plural4-rules.txt', encoding='utf-8') as pattern_file:
    for line in pattern_file:
        #split -> None, split qualquer espaço em branco; 3 -> splita 3 vezes
        pattern, search, replace = line.split(None, 3)
        rules.append(build_match_and_apply_functions(
            pattern, search, replace))

def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)
