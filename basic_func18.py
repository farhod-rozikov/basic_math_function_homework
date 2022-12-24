from math import pi


def main(a):
    '''Assign the value pi to the parametr "a". Round the result to 2 decimal places and return it.
    
    Args:
        a (float): a number
        
    Returns:
        float: the result.
    '''
    result = round(a, 2)
    return result

print(main(pi))