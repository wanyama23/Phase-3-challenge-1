# : Two numbers are positive.

def check_positive_numbers(a, b, c):
    if a >= 0 and b >= 0 and c >= 0:
        return True
    elif a<=0 and b>=0 and c>=0:
        return True
    elif a>0 and b<0 and c>0:
        return True        
    else:
        return False

print(check_positive_numbers(-2, 5, 1))