class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort()
        odd=[]
        even=[]
        final=[]
        for i in range(len(nums)):
            if(nums[i]%2==0):
                even.append(nums[i])
            else:
                odd.append(nums[i])
        final.extend(even)
        final.extend(odd)
        return(final)
