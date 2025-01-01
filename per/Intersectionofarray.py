from collections import Counter
def arraysIntersection(arr1,arr2,arr3):
    a2 = Counter(arr2)
    a3 = Counter(arr3)
    res = []
    for num in arr1:
        if num in a2 and num in a3:
            res.append(num)
    return res
arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]
print(arraysIntersection(arr1,arr2,arr3))