def main(N):
    """
    The number N is given. Calculate the sum below: 1 + 1/2 + 1/3 + … + 1/N.
    Args:
        N: int
    Returns:
        float: return  answer
        

    """
    for i in range(0,N+1):
        str(i)+=str(len(i))
    return i
b = int(input())
print(main( b))