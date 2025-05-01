def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    if B>=A:
        return list(range(B,A-1,-1))
    return list(range(B,A+1))
a = int(input())
b = int(input())
print(main(a, b))