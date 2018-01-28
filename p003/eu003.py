"""
Project Euler: Problem #003
"""

import math

def eu003(num):
    """
    TODO: add info
    """
    
    # check validity of input
    assert(num >= 0)
    
    # check 1 & 2
    if num < 2: 
        return num
        
    res = []
    
    # reduce even
    while num % 2 == 0:
        res.append(2)
        num //= 2
        
    # reduce odd
    lim = math.sqrt(num)
    i = 3
    
    while i <= lim:
    
        if num % i == 0:
            res.append(i)
            num //= i
            lim = math.sqrt(num)
            
        else:
            i += 2
            
    if num != 1:
        res.append(num)
        
    return max(res)
        