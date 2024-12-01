
def isSubstringPresent(s):
         l = 0
         r = 1
         
         arr = []
         reversed_string = ""
         for i in range(len(s) - 1, -1, -1):
              reversed_string += s[i]
    
         while r < len(s):
               arr.append(s[l:r+1:1])
               l+=1
               r+=1
         l =0
         r = 1
         while r < len(reversed_string):
                if s[l:r+1:1] in arr:
                       return True
                r+=1
                l+=1
    
         return False
     
s = "leetcode"
print(isSubstringPresent(s))