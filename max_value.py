def max_value(nums):
  max=float("-inf")

  for i in nums:
    if i >max:
      max=i

  return(max)

# Test with a positive list of numbers
nums1 = [1, 2, 3, 4, 5]
print(max_value(nums1))  # Expected output: 5

# Test with a list containing negative numbers
nums2 = [-1, -2, -3, -4, -5]
print(max_value(nums2))  # Expected output: -1

# Test with a mix of positive and negative numbers
nums3 = [-1, 2, 0, 5, -4]
print(max_value(nums3))  # Expected output: 5

# Test with a list of identical numbers
nums4 = [7, 7, 7, 7]
print(max_value(nums4))  # Expected output: 7

# Test with an empty list (handle edge case)
nums5 = []
print(max_value(nums5))  # This will return -inf, or you might add code to handle empty lists



