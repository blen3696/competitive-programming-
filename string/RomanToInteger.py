def romanToInt( s):
        """
        :type s: str
        :rtype: int
        """
        no = 0
        my_dict = {} 
        my_dict.update({"I": 1, "V": 5,"X":10,"L":50,"C":100,"D":500,"M":1000})

        for i in range(len(s) - 1, -1, -1):
            if my_dict[s[i]] < my_dict[s[i-1]]:
                no = no -my_dict[s[i]]
            else:
               no = no + my_dict[s[i]] 
        return no
    
print(romanToInt("LVIII"))