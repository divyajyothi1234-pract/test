def add(a,b):
    """
    This function takes two numbers and returns their sum.
    """
    return a + b    

def even_odd(num):
    """
    This function checks if a number is even or odd.
    Returns 'even' if the number is even, otherwise returns 'odd'.
    """
    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'
    
print(add(2, 3))  # Example usage of the add function
print(even_odd(4))  # Example usage of the even_odd function