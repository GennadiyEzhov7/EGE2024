for n in range(1000, 10000):
    st = str(n)
    t = st[0]
    s = st[1]
    d = st[2]
    e = st[3]
    p1 = int(t)+int(s)
    p2 = int(s)+int(d)
    p3 = int(d)+int(e)
    if p1 < p2 and p1 < p3:
        if p2 < p3:
            r = str(p2)+str(p3)
        else:
            r = str(p3)+str(p2)
    elif p2 < p1 and p2 < p3
        if p1 < p3:
            r = str(p1)+str(p3)
        else:
            r = str(p3)+str(p1)
    else:
        if p2 < p3:
            r = str(p2)+str(p3)
        else:
            r = str(p3)+str(p2)
