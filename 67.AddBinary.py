result = []
    carry = 0

    i, j = len(a) - 1, len(b) - 1

    while i >= 0 or j >= 0 or carry:
        total = carry

        if i >= 0:
            total += int(a[i])
            i -= 1

        if j >= 0:
            total += int(b[j])
            j -= 1

        result.append(str(total % 2))  # Add the current bit
        carry = total // 2             # Update the carry

    return ''.join(reversed(result))


#simplest approach

class Solution(object):
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]

