#roman1.py
import re

roman_numeral_map = (('M', 1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C', 100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX',  9),
                     ('V',   5),
                     ('IV',  4),
                     ('I',   1))
biggest_roman_number = 3999
smallest_roman_number = 1

roman_numeral_pattern = re.compile('''
    ^                   # beginning of string
    M{0,3}              # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                        #            or 500-800 (D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                        #        or 50-80 (L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                        #        or 5-8 (V, followed by 0 to 3 Is)
    $                   # end of string
    ''', re.VERBOSE)

def to_roman(n : int) -> str:
    result = ''

    if not isinstance(n, int):
        raise NotIntegerError("Numerais romanos apenas representam números INTEIROS")

    if not smallest_roman_number <= n <= biggest_roman_number:
        raise OutOfRangeError("Número fora do alcance aceitável (1...3999)")

    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
    return result

def from_roman(s):
    '''Converte um numeral romano para integer'''
    if not roman_numeral_pattern.search(s):
        raise InvalidNumeralError('Numeral romano inválido: {0}'.format(s))
    index = 0
    result = 0
    for numeral, integer in roman_numeral_map:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)   

    return result


class OutOfRangeError(ValueError):
    '''Valor fora do alcance do numeral romano'''

class NotIntegerError(ValueError):
    '''Valor não é integer (numerais romanos não trabalham com números reais)'''

class InvalidNumeralError(ValueError):
    '''Numeral passado não é um numeral romano válido'''