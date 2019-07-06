"""
Project Euler: Problem #005
"""

def solve(max):
    """
    Naive implementation with dumb mod-divisions (with some speed enhancements).
    
    .. note:: There is a purely mathematical solution.

    :param max: Max divisor.
    :returns: The smaller numbers that is evenly divisible by all of the numbers from 1 to ``max``.
    """
    
    n = max
    
    while True:
        for d in range(max, 2, -1):    # <-- inverse range for slight speed improvement
            if n % d: break
         
        else:
            break
        
        n += max
                       
    return n

    
# Independent driver
if __name__ == '__main__':
    print("Check: {}".format(solve(20)))