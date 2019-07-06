"""
Project Euler: Problem #004
"""

from math import pow

def solve(digits):
    """
    Naive implementation with nested palindrome function.

    :param digits: Number of digits that product numbers made of.
    :returns: The largest palindrome.
    """
    
    def pali(inp):
        d = inp
        r = 0
        
        while d:
            r = r * 10 + d % 10
            d //= 10
        
        if r == inp: return r
        else: return 0
        
    p = 0        
    max = 10**digits
   
    for m in range(max-1, max//10, -1):
    
        n = max-1
        
        while n >= m:
        
            if m*n < p: break  # <-- optimization
            
            if pali(m * n) > p: p = m * n
            
            n -= 1
                       
    return p
        