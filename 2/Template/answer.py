print('x y z w') #вывод переменных для видимости
for x in range(2): #перебор для x
    for y in range(2): #перебор для y
        for z in range(2): #перебор для z
            for w in range(2): #перебор для w
                if ((x == (not y))<=((x and w) == (z and (not w)))) == False: #выражение(обязательно взять все в скобки!)
                    print(x, y, z, w) #вывод таблицы
print('* * * *') #подставить результат(гарантия)
