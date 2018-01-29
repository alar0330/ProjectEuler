"""
Project Euler: Problem #001
"""


def eu001(lim = 1000):
    """
    Naive implementation with sum over a generator
    """

    return sum(x for x in range(lim) if (x % 3 == 0) or (x % 5 == 0))