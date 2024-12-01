
def kthDistinct(arr, k):
    frequencies = {}
    for element in arr:
         if element in frequencies:
             frequencies[element] += 1
         else:
             frequencies[element] = 1
    arr =[]
    for element, frequency in frequencies.items():
         if frequency == 1:
              arr.append(element)
    n = len(arr)
    if n < k:
        return " "
    
    return arr[k-1]
arr =["d","b","c","b","c","a"]
print(kthDistinct(arr,2))