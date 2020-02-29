# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    res = 0
    from_ = from_%60
    to = to % 60

    if from_>to:
        to+=60
        
    def fib(n):
        if n<=1:
            return n
        prev = 0
        curr = 1
        for i in range(n-1):
            prev, curr = curr, (prev+curr)%10
        return curr
    

    
    for i in range(from_,to + 1):
        res = (res+fib(i))%10
        
    return res


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
