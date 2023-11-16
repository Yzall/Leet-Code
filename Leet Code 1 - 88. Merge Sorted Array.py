# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
#   representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
#   and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


# Solution 1
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Initialize pointers for nums1 and nums2
        p1, p2 = m - 1, n - 1
        # Initialize the end of the merged array
        end = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[end] = nums1[p1]
                p1 -= 1
            else:
                nums1[end] = nums2[p2]
                p2 -= 1
            end -= 1

        # If there are remaining elements in nums2, copy them to nums1
        while p2 >= 0:
            nums1[end] = nums2[p2]
            p2 -= 1
            end -= 1


# Solution 2
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for j in range(n):
            nums1[m + j] = nums2[j]
        nums1.sort()
