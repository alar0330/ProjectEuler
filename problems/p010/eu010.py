"""
Project Euler: Problem #010
"""

from math import sqrt

def eu010(lim):
    """Slightly optimized straight-forward 
    prime number generator below the input limit.
    
    :param lim:  Upper limit to generate prime number up to.
    :returns:    Returns the sum of all primes below lim.
    """
    
    def nextPrime(lim):
        """Prime number generator."""

        yield 2
        
        p = 3
        
        while p < lim:
        
            for d in range(3, int(sqrt(p))+1, 2):
                if not p % d: break
            
            else: 
                yield p
                
            p += 2

            
    return sum(n for n in nextPrime(lim))
    
# Independent driver
if __name__ == '__main__':
    print("Check: {}".format(eu010(2*1000*1000)))
    print("TMP")
