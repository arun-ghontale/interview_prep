from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valid_nums = [num for num in nums if num != val]

        ind = 0
        while ind < len(valid_nums):
            nums[ind] = valid_nums[ind]
            ind += 1

        return len(valid_nums)

    def removeElementEfficient(self, nums: List[int], val: int) -> int:
        n_valid = 0

        for ind in range(len(nums)):
            if nums[ind] != val:
                nums[n_valid] = nums[ind]
                n_valid += 1

        return n_valid


def main():
    soln = Solution()
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(soln.removeElement(nums=nums, val=val))


if __name__ == '__main__':
    main()