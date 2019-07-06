"""
Project Euler: Problem #003
"""

from math import sqrt

def solve(num):
    """
    Solve by factorizing the input parameter.

    :param num: Number to factorize.
    :returns: The largest prime factor.
    """
    
    # check validity of input
    assert(num >= 0)
    
    # check 0 & 1
    if num < 2: 
        return num
        
    res = []
    
    # reduce even
    while num % 2 == 0:
        res.append(2)
        num //= 2
        
    # reduce odd
    lim = sqrt(num)
    i = 3
    
    while i <= lim:
    
        if num % i == 0:
            res.append(i)
            num //= i
            lim = sqrt(num)
            
        else:
            i += 2
            
    if num != 1:
        res.append(num)
        
    return max(res)
        