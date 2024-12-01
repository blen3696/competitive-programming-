def max_length(str: str) -> int:
 
  S = list(str) 
  i = 0
  while i < len(S) - 1:
    if S[i] == 'A' and S[i + 1] == 'B':
      del S[i:i + 2]  
      i = 0 
    elif S[i] == 'C' and S[i + 1] == 'D':
      del S[i:i + 2]  
      i = 0 
    else:
      i += 1

  return len(S)  


str = "AABAB"
result = max_length(str)
print(result) 
