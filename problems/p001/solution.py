"""
Project Euler: Problem #001
"""


def solve(lim = 1000):
    """
    Naive implementation with sum over a generator

    :param lim: Max number to sum up to.
    :returns: The sum of the filtered components.
    """   

    return sum(x for x in range(lim) if (x % 3 == 0) or (x % 5 == 0))