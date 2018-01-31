"""
Project Euler: Problem #002
"""

def eu002(lim = 4 * 1000 * 1000):
    """
    Naive solution with a function.

    :param lim: Max number to sum up to.
    :returns: The sum of the odd Fibo-numbers.
    """    
    
    a, b = 0, 1
    sum = 0
    
    while b < lim:
    
        a, b = b, a + b       # <-- tuple assignment to avoid tmp var
        
        if not b % 2: 
            sum += b
    
    return sum
    
def eu002_alt(lim):
    """
    Alternative solution using a generator.
    
    **Note**: Must sum over the generator at the end.
    
    :param lim: Max number to sum up to.
    :returns: The sum of the odd Fibo-numbers.
    """
    
    def numGen(lim):
    
        a, b = 1, 2
        
        while a < lim:
        
            if not a % 2: 
                yield a           # <-- generator
                
            a, b = b, a + b       # <-- tuple assignment to avoid tmp var
        
    return sum(numGen(lim))