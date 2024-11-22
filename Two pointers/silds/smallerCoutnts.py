def countSmaller(nums1, nums2):
    arr = []
    l = 0
    r = 0
    while r < len(nums2):
        while l < len(nums1) and nums1[l] < nums2[r]:
            l+=1
        
        arr.append(l)
        r +=1
    return arr
n1 = [2,2,5,6]
n2 = [3,4,6,8]
print(countSmaller(n1,n2))
        