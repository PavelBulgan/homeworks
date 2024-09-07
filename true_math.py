from math import inf

def divide(first ,second):
    rez = 0
    if second == 0:
        return inf
    else:
        rez = first / second
    return rez

#divide(20, 0)