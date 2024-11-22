def checkInclusion( p, s):
    
    Pcount = {}
    Scount = {}
   
    for i in range(len(p)):
        Pcount[p[i]] = 1 + Pcount.get(p[i],0)
        Scount[s[i]] = 1 + Scount.get(s[i],0)
    if Pcount == Scount:
        return True
    
    l =0
    for r in range(len(p), len(s)):
        Scount[s[r]] = 1 + Scount.get(s[r],0)
        Scount[s[l]] -=1
        if Scount[s[l]] == 0:
            Scount.pop(s[l])
        
        l+=1
        
        if Scount == Pcount:
            return True
    return False
s1 = "hello"
s2 = "ooolleoooleh"
print(checkInclusion(s1,s2))