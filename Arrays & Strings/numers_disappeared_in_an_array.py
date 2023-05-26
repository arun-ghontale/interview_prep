from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        all_nums_set = set([num for num in range(1, len(nums) + 1)])

        return list(all_nums_set - nums_set)


def main():
    soln = Solution()

    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(soln.findDisappearedNumbers(nums))


if __name__ == '__main__':
    main()
