def numerics(n):
    return [int(i) for i in str(n)]

def kaprekar_check(n):
    l = numerics(n)
    check1 = not (len(set(l)) == 1)
    check2 = not ((n == 100) or (n == 1000) or (n == 100000))
    check3 = (len(l) == 3 or len(l) == 4 or len(l) == 6)
    return check1 and check2 and check3

def kaprekar_step(digits):
    min_number_str = ''.join(map(str, sorted(digits)))
    return int(min_number_str[::-1]) - int(min_number_str)

def kaprekar_loop(n):
    if not kaprekar_check(n):
        print(f"Ошибка! На вход подано число {n}, не удовлетворяющее условиям процесса Капрекара")
    else:
        print(n)
        lst = []
        while n not in [495, 6174, 549945, 631764]:
            n = kaprekar_step(numerics(n))
            if n not in lst:
                print(n)
                lst.append(n)
            else:
                print(f"Следующее число - {lst[lst.index(n)]}, кажется процесс зациклился...")
                return
