def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    x1=n%10
    n=n//10
    x2=n%10
    n=n//10
    x3=n%10
    n=n//10
    x4=n%10
    n=n//10
    x5=n%10
    n=n//10

    m = x1
    if m<x2:
        m=x2
    if m<x3:
        m=x3
    if m<x4:
        m=x4
    if m<x5:
        m=x5
        
    return m