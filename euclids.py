
def euclids_algorithm(m: int, n: int) -> int:
    """
    Given unsigned int m, n. Find the highest common denominator.
    :rtype: int
    :param m: first number in question
    :param n: second number in question
    :return: Highest common denominator
    """
    # Check if m is greater than n to skip the first loop.
    if m < n:
        m, n = n, m

    # Initialize the remainder value.
    r = 1
    while r:
        r = m % n
        if r != 0:
            m = n
            n = r

    return n
