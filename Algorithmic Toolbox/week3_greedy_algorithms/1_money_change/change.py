# Uses python3
import sys

def get_change(m):
    res = 0
    while m>0:
        if m//10 !=0:
            res += m//10
            m = m%10
        elif m //5!=0:
            res += m//5
            m = m%5
        else:
            res+=m
            m = 0
    return res

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
