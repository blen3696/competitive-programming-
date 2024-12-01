def canBeTypedWords( text, brokenLetters):
     words = text.split() 
     count = 0 
     for word in words:
         can_type = True 
         for letter in word:
             if letter in brokenLetters: 
                  can_type = False
                  break
         if can_type:
             count += 1
     return count
 
text = "hello world"
brokenLetters = "ad"
print(canBeTypedWords(text,brokenLetters))