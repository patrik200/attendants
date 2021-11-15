clear = "\n" * 300
print (clear)
print('[0]выбор счёта\n[1]плотность')
a = int(input('номер: '))
print (clear)
if a == 1:
    print('p=m/v\nm=pv\nv=m/p')
    print(clear)
elif a == 0:
    print('[1]плотность')
    x = int(input('что нужно найти? '))
    print(clear)
    if x == 1:
        ma = int(input("в чём масса?\n[1]в тоннах?\n[2]в килограммах?\n[3]в граммах? "))
        print(clear)
        va = int(input('в чём объём?\n[1]в метрах?\n[2]в литрах?\n[3]в сантиметрах? '))
        print(clear)
        ma1 = int(input('а в чём нада масса?\n[1]в килограммах?\n[2]граммах? '))
        print(clear)
        ma2 = int(input('кол-во массы: '))
        print(clear)
        va2 = int(input('кол-во объёма '))


        if ma1 == 1:
            va1 = 1;
        elif ma1 == 2:
            va1 = 3;



        if ma == 1 and ma1 == 1:
            ma3 = ma2 * 1000
        elif ma == 1 and ma1 == 2:
            ma3 = ma2 * 1000*1000
        elif ma == 2 and ma1 == 1:
            ma3 = ma2
        elif ma == 2 and ma1 == 2:
            ma3 = ma2 * 1000
        elif ma == 3 and ma1 == 1:
            ma3 = ma2/1000
        elif ma == 3 and ma1 == 2:
            ma3 = ma2
        if va == 1 and va1 == 1:
            va3 = va2
        elif va == 1 and va1 == 2:
            va3 = va2 * 1000
        elif va == 1 and va1 == 3:
            va3 = va2 * 1000000
        elif va == 2 and va1 == 1:
            va3 = va2/1000
        elif va == 1 and va1 == 2:
            va3 = va2
        elif va == 1 and va1 == 2:
            va3 = va2 * 1000
        if ma1 == 1:
            p = ma3/va3
            print(p, "кг/м^3")