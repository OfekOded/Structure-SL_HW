# Oded Ofek 215348145
# Ziv Farajun 323920603
import math


def getPentaNum(n):
    return n*(3*n-1)/2

def pentaNumRange(n1,n2):
    return list(map(getPentaNum,range(n1,n2)))

def sumDigit(n):
    return sum(list(int(x) for x in str(n)))


gematria = {
    'א': 1,
    'ב': 2,
    'ג': 3,
    'ד': 4,
    'ה': 5,
    'ו': 6,
    'ז': 7,
    'ח': 8,
    'ט': 9,
    'י': 10,
    'כ': 20,
    'ל': 30,
    'מ': 40,
    'נ': 50,
    'ס': 60,
    'ע': 70,
    'פ': 80,
    'צ': 90,
    'ק': 100,
    'ר': 200,
    'ש': 300,
    'ת': 400,
    'ך': 20,
    'ם': 40,
    'ן': 50,
    'ף': 80,
    'ץ': 90
}

def gmCalculator(str):
    return sum(list(gematria.get(letter) for letter in str))

def is_prime(n):
    if n <= 1:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    potential_divisors = range(5, int(math.sqrt(n)) + 1, 6)

    return all(n % i != 0 and n % (i + 2) != 0 for i in potential_divisors)

def twinPrime(n):
    if is_prime(n-2):
        return n-2
    elif is_prime(n+2):
        return n+2
    else:
        return False

def myPrime(n):
    keys = list(filter(twinPrime,list(filter(is_prime, range(1, n+1)))))
    values = list(map(twinPrime,keys))
    return dict(zip(keys,values))

def multi(n):
    return n*2

def pow(n):
    return n*n

def inverse(n):
    if n!=0:
        return 1/n
    else:
        return "ERROR"

function = [multi,pow,inverse]

def apply_functions(numbers, functions):
    keys = list(functions)
    values = [list(map(func, numbers)) for func in functions]
    return dict(zip(keys, values))

if __name__ == '__main__':
   print(apply_functions([1, 2, 3, 4, 5],function))