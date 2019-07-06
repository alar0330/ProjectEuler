"""
Project Euler: Problem #009
"""


def solve(s):
    """After a short analytic transformation, the
    algorithm searches for an integer value that solves the 
    derived equation by iterating through all possibilities.
    
    :param s: Constraint on sum, i.e. s = a + b + c
    :returns: Returns the product a*b*c.
    """
    
    # Solve 2 eqs. for 'b' in terms of 'a'
    b = lambda a: ( s*a - s*s/2 ) / ( a - s )
    
    for a in range (1, s - 1):
        if b(a).is_integer():
            break
            
    c = s - a - b(a)
                 
    return int(a*b(a)*c)
    
# Independent driver
if __name__ == '__main__':
    print("Check: {}".format(solve(12)))
