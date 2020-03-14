class Solution:
    
    def numTrees(self, n):
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        elif n>1:
            nums = 0
            numList = {0:0,1:1}
            for i in range(2,n+1):
                nums = 2*numList[i-1]
                for j in range(1,(i+1)//2):
                    if j == i - j -1:
                        nums = nums + numList[j] ** 2
                    else:
                        nums = nums + 2* numList[j] * numList[i-j-1]
                numList[i] = nums


        
        return nums
        

solute = Solution()
solute.numTrees(3)
                