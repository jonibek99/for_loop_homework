def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    b=[]
    for i in list1:
        b.append(str(i)[:3])
    return b
list1=['jonibek','shac','husan','me,003',9333]
print(main(list1))


