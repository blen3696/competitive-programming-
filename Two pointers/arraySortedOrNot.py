def arraySortedOrNot(self, arr) -> bool: #o(n) o(1)
        
        l = 0
        
        for r in range(1, len(arr)):
            if arr[l] > arr[r]:
                return False
            if arr[l] <= arr[r]:
                l +=1
        return True