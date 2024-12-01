def merge( nums1, m, nums2, n):
    r= 0
    for i in range(m+n):
        if nums1[i] <= nums2[r]:
            l+=1
        else:
            nums1[i] = nums2[r]
            for i in range(l+1, m+n):
                nums1[i],nums1[i-1] = nums1[i-1], nums1[i]
            r+=1
            l+=1
    return nums1
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(merge(nums1,m,nums2,n))