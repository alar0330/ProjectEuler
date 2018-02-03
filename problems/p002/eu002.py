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
    
        if not b % 2: 
            sum += b
            
        a, b = b, a + b       # <-- tuple assignment to avoid tmp var
    
    return sum
    
def eu002_alt(lim):
    """
    Alternative solution using a generator.
    
    **Note**: Must sum over the generator at the end.
    
    :param lim: Max number to sum up to.
    :returns: The sum of the odd Fibo-numbers.
    """
    
    def numGen(lim):
    
        a, b = 0, 1
        
        while b < lim:
        
            if not b % 2: 
                yield b           # <-- generator
                
            a, b = b, a + b       # <-- tuple assignment to avoid tmp var
        
    return sum(numGen(lim))
    
    
if __name__ == '__main__':
    print("Check: {}".format(eu002(100)))