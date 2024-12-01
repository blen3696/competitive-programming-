def firstUniqChar( s):
   
     frequencies = {}
     for element in s:
          if element in frequencies:
             frequencies[element] += 1
          else:
             frequencies[element] = 1
   
     for i in range(len(s)):
         if frequencies[s[i]] == 1:
             return i
             
     return -1 
  
s =  "leetcode"
print(firstUniqChar(s))