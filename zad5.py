def convector(n, osn):
    s=""
    while n>0:
        s += str(n % osn)
        n //= osn
    return s[::-1]
def Result(n):
    r = convector(n, 2)
    if r.count('2')%2==0:
        r = '11'+r+'11'
    else:
        r = '11'+r+'11'
    return int(r, 2)
print(max(x for x in range(1, 10000) if Result(x) < 3799))
# Памятка 
# r =''.join(sorted(str(r), reverse=True)) сортироввка по убыванию 3 2 1
# r = r[2:0] срезы, берет от 2 до конца
# r = r[0:-2] срез наоброт, берет от 2 с конца и до начала
# print(min(range(10,1000), key=R)) при отсутсвии условий с R и N разом
# sums = sum(int(d) for d in r) сумма всех чисел в r (если условно 3-я система)



