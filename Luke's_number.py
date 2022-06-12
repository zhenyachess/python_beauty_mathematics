def L6n(n):
    L = super_L(n)
    return L**6 - 6*(-1)**n * L**4 + 9*L**2 - 2*(-1)**n
    
def L5n(n):
    L = super_L(n)
    return L**5 - 5*(-1)**n * L**3 + 5*L   
    
def L4n(n):
    L = super_L(n)
    return L**4 - 4*(-1)**n * L**2 + 2

def L3n(n):
    L = super_L(n)
    return L**3 - 3*(-1)**n * L

def L2n(n):
    L = super_L(n)
    return L**2 - 2*(-1)**n
    
def super_L(n):
    if n==0: return 2
    elif n==1: return 1
    elif not n%6: return L6n(n//6)
    elif not n%5: return L5n(n//5)
    elif not n%4: return L4n(n//4)
    elif not n%3: return L3n(n//3)
    elif not n%2: return L2n(n//2)
    else: return super_L(n-1)+super_L(n-2)
    
# Written by https://stepik.org/users/61929697
