# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


# Solution 1:
class Solution(object):
    def strStr(self, haystack, needle):
        return haystack.find(needle)


# Solution 2:
class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i

        return -1


sol = Solution()
var1 = "sadbutsad"
var2 = "sad"
print(sol.strStr(var1, var2))
