#FirstBadVersion
class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n
        result = 0
        while low <= high:
            x = math.ceil((low + high)/2)
            if isBadVersion(x) == True:
                result = x
                high = x - 1
            else:
                 low = x + 1
        return(result)
