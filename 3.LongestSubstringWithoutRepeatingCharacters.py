class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_map = {}
        start = 0
        max_length = 0

        for i, char in enumerate(s):
            if char in char_map and char_map[char] >= start:
                start = char_map[char] + 1
            char_map[char] = i  # Update last seen index
            max_length = max(max_length, i - start + 1)

        return max_length
