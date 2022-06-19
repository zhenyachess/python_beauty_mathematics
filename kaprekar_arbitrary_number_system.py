def convert(num, to_base=10, from_base=10):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decimal = int(str(num), from_base)
    target = ""
    while decimal > 0:
        target = alpha[decimal % to_base] + target
        decimal = decimal // to_base
    return target

def kaprekar_10(n):
    s = str(n**2)
    for i in range(1,len(s)):
        a = s[:i]
        b = s[i:]
        if int(b)!=0 and int(a) + int(b) == n:
            return True
    return False

def kaprekar(n, base=10):
    if base == 10:
        return kaprekar_10(n)
    else:
        num = int(convert(n, to_base=10, from_base=base))
        dec = num
        num = convert(num**2, base)
        for i in range(1, len(num)):
            a = convert(num[:i], to_base=10, from_base=base)
            b = convert(num[i:], to_base=10, from_base=base)
            if dec == int(a) + int(b):
                return True
        return False
