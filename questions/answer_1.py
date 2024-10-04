

def addNumbers(a: float, b: float) -> int:
    if not (0.1 < a < 10**6 and 0.1 < b < 10**6):
        raise ValueError("Input numbers must be between 0.1 and 10^6") 
    if (len(str(a).split(".")[-1]) > 8) or (len(str(b).split(".")[-1]) > 8):
        raise ValueError("Input numbers have at most 8 places after the decimal")
    return int(a + b)