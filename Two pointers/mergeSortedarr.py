def mergearr(s, p):
    arr = []
    l = 0
    r = 0
    while l < len(s) and r < len(p):
        if s[l] <= p[r]:
            arr.append(s[l])
            l +=1
        else:
            arr.append(p[r])
            r +=1
    arr.extend(s[l:])
    arr.extend(p[r:])
    return arr
    
s = [1,2,5,6]
p = [3,4,7]
print(mergearr(s,p))
