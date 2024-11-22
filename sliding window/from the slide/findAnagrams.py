def findAnagrams(self, s, p): # o(n) o(n)
    if len(p) > len(s): return []
    Pcount = {}
    Scount = {}
   
    for i in range(len(p)):
        Pcount[p[i]] = 1 + Pcount.get(p[i],0)
        Scount[s[i]] = 1 + Scount.get(s[i],0)
    if Pcount == Scount:
        res = [0]
    else:
        res = []
    l =0
    for r in range(len(p), len(s)):
        Scount[s[r]] = 1 + Scount.get(s[r],0)
        Scount[s[l]] -=1
        if Scount[s[l]] == 0:
            Scount.pop(s[l])
        l+=1
        
        if Scount == Pcount:
            res.append(l)
    return res