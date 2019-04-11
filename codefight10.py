def deleteChar(string,position):
    newString = ""
    for i in range(len(string)):
        if(i == position):
            continue;
        else:
            newString = newString + string[i]
    return newString


def commonCharacterCount(s1, s2):
    ch = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if(s1[i] == s2[j]):
                s2 = deleteChar(s2,j)
                ch = ch + 1
                break
        continue
    return ch


s1 = "Ammar"
s2 = "abdullah"
print(commonCharacterCount(s1,s2))
    
