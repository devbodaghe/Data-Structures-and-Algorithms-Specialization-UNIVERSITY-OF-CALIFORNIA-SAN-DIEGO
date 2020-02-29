# Uses python3
import sys

def fibonacci_partial_sum_naive(m, n):
    
    m %= 60
    n %= 60
   
    if m > n:
        n += 60
   
    fibList = [0, 1]
    fibSum = 0
    for i in range(1, n+1):
        if i > 1:
            temp = fibList[1]
            fibList[1] = fibList[0] + fibList[1]
            fibList[0] = temp
        if i >= m:
            fibSum = (fibSum + (fibList[1])%10) % 10
    return fibSum



if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
