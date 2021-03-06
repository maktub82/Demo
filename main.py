import sys
from utils.args import get_argument, get_integer_argument
from providers.fib import fib
from providers.factorial import factorial
from providers.calcs import mult, pot, div, mod

def main(argv):
    method = get_argument(argv, 0)
    if method == "fib":
        fib(get_integer_argument(argv, 1))
    elif method == "fac":
        factorial(get_integer_argument(argv, 1))
    elif method == "mult":
        mult(get_integer_argument(argv, 1), get_integer_argument(argv, 2))
    elif method == "pot":
        pot(get_integer_argument(argv, 1), get_integer_argument(argv, 2))
    elif method == "div":
        div(get_integer_argument(argv, 1), get_integer_argument(argv, 2))
    elif method == "mod":
        mod(get_integer_argument(argv, 1), get_integer_argument(argv, 2))
    else:
        print("The method is not valid")

if __name__ == "__main__":
    main(sys.argv[1:])
