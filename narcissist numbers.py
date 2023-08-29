def narcissistic( value ):
    num = []
    while value > 0:
        num.append(value % 10)
        value = value // 10

    long = len(num)
    total = 0

    for potencia in num:
        resul = potencia**long
        total += resul

    num.reverse()
    s = ''.join(map(str, num))
    n = int(s)

    if total == n:
        return True
    else:
        return False

print(narcissistic(153))