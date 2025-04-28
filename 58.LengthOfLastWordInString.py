class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        index = s.rfind(' ')
        if index == -1:
            return len(s)
        else:
            count = 0
            for char in range(index+1, len(s)):
                count = count +1
            return count
