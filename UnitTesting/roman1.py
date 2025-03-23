#roman1.py


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