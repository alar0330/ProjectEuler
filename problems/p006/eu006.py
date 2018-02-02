"""
Project Euler: Problem #006
"""

def eu006(max):
    """
    Semi-brute-force solution (using only arith. series formula).
    
    .. note:: There is a purely mathematical solution.
    
    .. warning:: I UNintentionally overloaded built-in max-function :)

    :param max: Max number in the series.
    :returns: The difference of the sum of the squares and the square of the sum.
    """

    sqSum = sum(x**2 for x in range(max+1))
    sumSq = ( (1 + max) * max / 2 )**2
    
    return int(sumSq - sqSum)
    
    
def eu006_alt(max):
    """
    Analytic solution.
    
    :param max: Max number in the series.
    :returns: The difference of the sum of the squares and the square of the sum.
    """

    sqSum = (2*max + 1) * (max + 1) * max / 6
    sumSq = ( (1 + max) * max / 2 )**2
    
    return int(sumSq - sqSum)
    
    
# Independent driver
if __name__ == '__main__':
    print("Check: {}".format(eu006(10)))
    print("Check (alt): {}".format(eu006_alt(10)))