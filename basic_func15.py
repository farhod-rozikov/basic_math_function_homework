from unittest import result


def main(a, b):
    '''Find the remainder when a is divided by b and return it.
    
    Args:
        a (int): a number
        b (int): a number
        
    Returns:
        int: the result.
    '''
    result = a % b
    return result

print(main(18, 5))