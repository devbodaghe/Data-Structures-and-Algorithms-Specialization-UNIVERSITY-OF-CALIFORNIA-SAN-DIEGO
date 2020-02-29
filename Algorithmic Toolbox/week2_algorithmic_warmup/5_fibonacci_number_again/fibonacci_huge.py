# Uses python3
import sys

def pisanoPeriod(m): 
    previous, current = 0, 1
    for i in range(0, m * m): 
        #print('i is' + str(i))
        previous, current=current, (previous + current) % m 
        #print(previous, current)
        
        if (previous == 0 and current == 1): 
            return i + 1

def get_fibonacci_huge_naive(n, m): 
      
    # Getting the period 
    pisano_period = pisanoPeriod(m) 
      
    # Taking mod of N with  
    # period length 
    n = n % pisano_period
    if n<1:
        return n
      
    previous, current = 0, 1
      
    for i in range(n-1): 
        previous, current = current, (previous + current)%m
          
    return current


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
