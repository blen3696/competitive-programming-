 # Brute force approach will be we take one element in outer ioop and we intialize inner loop and
# we intialize count = 0 then we compare arr[i] with arr[j] and if they are equal we increase count
# then if count > arr.len/ 2 we return arr[i]
def majorityElement( arr):
  """
  :type nums: List[int]
  :rtype: int
  """
  n = len(arr)
  frequencies = {}
  for element in arr:
    if element in frequencies:
      frequencies[element] += 1
    else:
      frequencies[element] = 1
  majority_element = -1
  for element, frequency in frequencies.items():
    if frequency > n/2:
      majority_element = element

  return majority_element  #Only return -1 if no majority element is found

   

# Example usage
arr = [3,3,4]
print(majorityElement(arr))



