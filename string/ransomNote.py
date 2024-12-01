def isransom(s, t):
 
 char_counts = {} 
 
 for char in s:
  if char in char_counts:
   char_counts[char] += 1
  else:
   char_counts[char] = 1

 
 for char in t:
  if char not in char_counts:
   return False 
  if char_counts[char] == 0:
   return False 
  char_counts[char] -= 1 

 return True 


s = "aa"
t = "aab"
print(isransom(s, t)) 
