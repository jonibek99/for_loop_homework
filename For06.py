def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    return sum(range(min(A, B), max(A, B) + 1))
a = int(input())
b = int(input())
print(main(a, b))