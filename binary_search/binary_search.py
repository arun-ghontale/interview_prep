from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(ind_start=0, ind_end=len(nums), nums=nums, target=target)

    def binary_search(self, ind_start: int, ind_end: int, nums: List[int], target: int) -> int:
        mid = ind_start + (ind_end - ind_start) // 2

        if (ind_end - ind_start) == 1 and target != nums[mid]:
            return -1

        elif target < nums[mid]:
            return self.binary_search(ind_start=ind_start, ind_end=mid, nums=nums, target=target)

        elif target > nums[mid]:
            return self.binary_search(ind_start=mid, ind_end=ind_end, nums=nums, target=target)

        else:
            return mid


def main():
    soln = Solution()

    nums = [-1, 0, 3, 5, 9, 12]
    target = 30000

    print(soln.search(nums=nums, target=target))


if __name__ == '__main__':
    main()
