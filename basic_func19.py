from unittest import result


def main(a, b):
    '''find the absolute value of the difference between a and b. Return it.
    
    Args:
        a (int): a number
        b (int): a number
        
    Returns:
        int: the result.
    '''
    result = abs(a - b)
    return result

print(main(5, 18))