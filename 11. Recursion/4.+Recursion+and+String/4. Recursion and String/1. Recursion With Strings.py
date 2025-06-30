def remove_character(s1,ch):
    if(len(s1)==0 or s1==''):
        return s1
    
    smallAnswer = remove_character(s1[1:],ch)

    if(s1[0]==ch):
        return smallAnswer
    else:
        return s1[0] + smallAnswer
    


s1 = "abczz"
ans = remove_character(s1,'z')
print(ans)


def remove_character2(s1, ch):
    if(len(s1) == 0 or s1 == ""):
        return s1
    if s1[0] == ch:
        return remove_character2(s1[1:], ch)
    else:                       
        return s1[0] + remove_character2(s1[1:], ch)
    


s2 = "abczzksnznszcx"
ans = remove_character2(s2,'z')
print(ans)