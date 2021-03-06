def mult(a,b):
    print(calc_mult(a,b))

def calc_mult(a, b):
    if b == 0:
        return 0
    else:
        return a + calc_mult(a,b-1)

def pot(b,n):
    print(calc_pot(b,n))

def calc_pot(b,n):
    if n <= 0:
        return 1
    if n % 2 == 0:
        pot = calc_pot(b, calc_div(n,2))
        return calc_mult(pot, pot)
    else:
        pot = calc_pot(b, calc_div((n-1),2))
        return calc_mult(calc_mult(pot, pot), b)

def div(a,b):
    print(calc_div(a, b))

def calc_div(a,b):
    if a <= b:
        return 0
    else:
        return 1 + calc_div(a-b,b)
    '''
    if a == b:
        return 1
    elif a < b:
        return 0
    else:
        return 1 + calc_div(a-b,b)
    '''

def mod(a, b):
    print(calc_mod(a,b))

def calc_mod(a,b):
    if a == b:
        return 0
    elif a < b:
        return a
    else:
        return calc_mod(a-b,b)
