def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    return str(list(range(0,n+1)))
a=int(input())
print(main(a))