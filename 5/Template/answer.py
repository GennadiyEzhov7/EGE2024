for n in range(0, 10000): #Перебор начального числа(от 1 до 9999)
    s = bin(n) #Создаем новую переменную где n записывается в двоичной системе
    s = s[2:]  #0b1011 -> 1011 -> RETURN STR
               #2: удаляет два символа слева
    s.count("1") #Так как s = str, счетаем кол-во единиц
    p1 = s.count("1")%2 #В переменную p1 заносим остаток от деления s.count на 2
    s = s + str(p1) #Складываем начальную s и p1(в строке)
    p2 = s.count("1")%2 #Повторяем, заносим остаток от деления s+p1 на 2 в переменную p2
    s = s + str(p2) #Складываем s+str(p1) + s+str(p2)
    r = int(s, 2)#Переводим получившееся s в 10-ую запись числа
                 #Int(n, система счисления)-> результат 10 число
    if r > 97: #По условию r должно быть больше 97
        print(n) #При этои условие выводим нужно нам N
        break #(не обязательно)Останавливает на минимальном значение
