# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.


class Solution(object):
    def lengthOfLastWord(self, s):
        # Remove leading and trailing whitespaces
        s = s.strip()

        # Initialize a variable to store the length of the last word
        last_word_length = 0

        # Iterate through the string from right to left
        for i in range(len(s) - 1, -1, -1):
            # Break when the first non-space character is encountered
            if s[i] != " ":
                last_word_length += 1
            else:
                # Break when a space is encountered after the last word
                break

        # Return the length of the last word
        return last_word_length


solution = Solution()
result = solution.lengthOfLastWord("Hello World")
print(result)
