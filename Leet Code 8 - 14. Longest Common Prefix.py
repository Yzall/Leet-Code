# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        # Sort the list of strings to ensure that the common prefix is at the beginning
        strs.sort()

        # Take the first and last strings (after sorting)
        first_str = strs[0]
        last_str = strs[-1]

        # Find the common prefix between the first and last strings
        common_prefix = []
        for i in range(len(first_str)):
            if i < len(last_str) and first_str[i] == last_str[i]:
                common_prefix.append(first_str[i])
            else:
                break

        # Convert the list of characters back to a string
        return "".join(common_prefix)


solution = Solution()
input_strings = ["flower", "flow", "flight"]
result = solution.longestCommonPrefix(input_strings)
print(result)
