class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
                return -1
        index = 0
        while haystack:
            if not haystack.startswith(needle):
                haystack = haystack[1:]
                index += 1
            else:
                return index
        return -1
        
