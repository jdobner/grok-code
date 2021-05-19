def comp(a: int, b: int):
    print(f'a={bin(a)}')
    print(f'b={bin(b)}\n')

    xor = a ^ b
    _or = a | b

    print(f'xor={bin(xor)}')
    print(f'_or={bin(_or)}')
    print(xor == _or)


def comp2(a: int, b: int):
    print(f'a={bin(a)}')
    print(f'b={bin(b)}\n')

    __or = a ^ b
    _sum = a + b

    print(f'__or={bin(__or)}')
    print(f'_sum={bin(_sum)}')
    return __or if __or == _sum else 0
