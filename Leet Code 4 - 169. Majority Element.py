# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# The Counter class is useful for counting the occurrences of elements in a collection.
from collections import Counter

class Solution(object):
    def majorityElement(self, nums):

        # Creates a Counter object, counter, by passing the array arr to it. 
        # This object will count the occurrences of each unique element in the array.
        counter = Counter(nums)

        # Retrieves a list of the most common elements. The argument 1 specifies that only the single most common element should be returned.
        most_common = counter.most_common(1)

        # The most_common result is a list of tuples where each tuple contains an element and its count. 
        # The [0][0] indexing is used to get the element from the first tuple. 
        # The if most_common else None part is a conditional expression that returns None if there are no elements in the array.
        most_common_elements = most_common[0][0] if most_common else None
        
        return most_common_elements

arr = [2,2,1,1,1,2,2]
sol = Solution()
test = sol.majorityElement(arr)

print(test)
