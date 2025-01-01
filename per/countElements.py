from collections import Counter

def countElements(arr):
    ctn = 0
    my_map = Counter(arr)
    s = set()
        
    for num in arr:
        if num + 1 in my_map and num not in s:
            ctn += my_map[num]
            s.add(num)
    return ctn
arr = [1,2,3,4]
print(countElements(arr))
            