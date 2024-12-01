def isAnagram( s, t):
 
      
    new1 = sorted(s)
    new2 = sorted(t)
    if(new1==new2):
            return True
    return False
    
        
s = "anagram"
t = "nagaramp"
print(isAnagram(s,t))