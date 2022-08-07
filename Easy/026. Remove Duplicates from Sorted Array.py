class Solution(object):
    def removeDuplicates(self, nums):
        lastNum = None
        write = 0

        for i in range(len(nums)):
            if nums[i] != lastNum:
                nums[write] = nums[i]
                lastNum = nums[i]
                write += 1

        return write