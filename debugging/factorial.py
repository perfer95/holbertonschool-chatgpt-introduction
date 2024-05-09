#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: {} <numero>".format(sys.argv[0]))
        sys.exit(1)

    f = factorial(int(sys.argv[1]))
    print(f)

