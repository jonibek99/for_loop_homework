def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    return sum(i for i in range(0,N+1) if i%2!=0)
b = int(input())
print(main( b))
        