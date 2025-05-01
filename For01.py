def main(n):
    """
    Return numbers from zero to n in a list view.
    Args:
        n: int
    Returns:
        list: return  answer
    """
    return list(range(0,n+1))
a=int(input())
print(main(a))