def isLucky(n):
    n = str(n)
    l = len(str(n))
    s1 = 0
    s2 = 0
    i = 0
    while i < (l/2):
        s1 = s1+int(n[int(i)])
        i = i+1
    i = l/2
    while i < l:
        s2 = s2 + int(n[int(i)])
        i = i + 1
    if(s1 == s2):
        return True
    else:
        return False
