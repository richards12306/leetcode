#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
import random
# @lc code=start
class Solution:
    def findKthLargest(self, nums,k):
        size = len(nums)
        if k > size:
            raise Exception('程序出错')

        L = []
        for index in range(k):
            # heapq 默认就是小顶堆
            heapq.heappush(L, nums[index])

        for index in range(k, size):
            top = L[0]
            if nums[index] > top:
                # 看一看堆顶的元素，只要比堆顶元素大，就替换堆顶元素
                heapq.heapreplace(L, nums[index])
        # 最后堆顶中的元素就是堆中最小的，整个数组中的第 k 大元素
        return L[0]



        #聪明的孩子在看到 K-top 问题的时候当然第一个反应应该是快排对不对，都已经分了边，就可以减少很多工作量
        
        # if len(nums)==1:
        #     return nums[0]

        # lNum=[]
        # rNum=[]
        # index = random.randint(0,len(nums)-1)
        # tag = nums[index]
        # sign = 0
        # for i in nums:
        #     if tag>i:
        #         lNum.append(i)
        #     elif tag < i:
        #         rNum.append(i)
        #     elif tag ==i:
        #         sign+=1
        # # print(k,lNum,tag,rNum)
        # if len(rNum) >=k:
        #     return self.findKthLargest(rNum,k)
        # #右侧数组不够 k 个
        # elif sign+len(rNum)>=k:
        #     return tag
        # #sign 加上右侧都不够 k 个
        # else:
        #     return self.findKthLargest(lNum,k-len(rNum)-sign)

nums=[3,2,1,5,6,4]
k=2
solute = Solution()
print(solute.findKthLargest(nums,k))
        
# @lc code=end

#极其朴素的方法，排序输出
        # nums.sort()
        # return nums[-k]

 #利用堆的信息
        # Heap = []
        # minIterm = nums[0]
        # for iterm in nums:
        #     if len(Heap) < k:
        #         Heap.append(iterm)
        #         minIterm = min(iterm,minIterm)
        #     else:
        #         if iterm > min(Heap):
        #             Heap.remove(minIterm)
        #             Heap.append(iterm)
        #             minIterm = min(Heap)

        # return minIterm
        #当然你也可以一句话完成任务
       # return heapq.nlargest(k, nums)[-1]