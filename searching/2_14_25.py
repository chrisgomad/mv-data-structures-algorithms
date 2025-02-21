#FirstBadVersion
class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = len(n)
        #Add result to store the least bad version that was found
        result = 0
        
        while low <= high:
            #rounding up to the nearest whole number
            x = math.ceil((low + high)/2)
            if isBadVersion(x) == True:
                result = x
                high = x - 1
            else:
                 low = x + 1
        return(result)
