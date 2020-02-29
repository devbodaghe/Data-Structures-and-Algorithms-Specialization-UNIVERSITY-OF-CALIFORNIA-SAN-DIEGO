# Uses python3
import sys

def hcf(a,b):
    if b == 0:
        return a
    c = a%b
    return hcf(b,c)

def lcm_naive(a,b):
    prod = a*b
    return prod//hcf(a,b)
#     for l in range(1, a*b + 1):
#         if l % a == 0 and l % b == 0:
#             return l

#     return a*b

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))
