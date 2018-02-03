"""
Project Euler: Problem #007
"""

from math import sqrt

def eu007(nth):
    """
    Memory-friendly and speed-optimized prime number generator.
    
    .. note: Could also have used 'itertools' module.
    
    :param nth: Position of the prime number in the series.
    :returns: Returns the calculated Nth prime number.
    """

    def isPrime(n):
        """Efficient prime number search algorithm."""
    
        if n <= 1: return False
        
        elif n <= 3: return True
        
        elif not n % 2: return False
        
        else:
        
            for d in range(3, int(sqrt(n))+1, 2):
                if not n % d: return False
                
            else:
                return True
    
    def nextPrime():
        """Prime number generator."""
    
        s = 2
        
        while True:
        
            while not isPrime(s):
                s += 1
            
            yield s
            s += 1
    
    
    p = nextPrime()         # <-- create generator object
    for _ in range(nth-1):  # <-- skip first 'nth-1' lines
        next(p)
        
    return next(p)          # <-- return 'nth'
    
    
# Independent driver
if __name__ == '__main__':
    print("Check: {}".format(eu007(1)))
