# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
# nums1 = [1, 3]
# nums2 = [2]
# The median is 2.0

# we are only interested in knowing what the left half of the merged array,
# A union B, would be, because this is the subarray that ends with the median.

