from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        numLen = len(nums)
        if numLen in [0, 1]:
            return numLen
        
        dp = [nums[0]]
        for i in range(1, numLen):
            if len(dp) < 2:
                if nums[i] - dp[-1] != 0:
                    dp.append(nums[i])
                else:
                    continue
            else:
                diff = dp[-1] - dp[-2]
                if diff > 0:
                    if nums[i] - dp[-1] < 0:
                        dp.append(nums[i])
                    elif nums[i] - dp[-1] >= 0:
                        dp[-1] = nums[i]
                else:
                    if nums[i] - dp[-1] > 0:
                        dp.append(nums[i])
                    elif nums[i] - dp[-1] <= 0:
                        dp[-1] = nums[i]
        
        return len(dp)
