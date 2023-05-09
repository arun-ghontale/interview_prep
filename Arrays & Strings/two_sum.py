from typing import List


class Solution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        nums_dict = dict()

        for ind, ele in enumerate(nums):
            other_number = target - ele
            if other_number not in nums_dict:
                nums_dict[other_number] = ind

        for ind, ele in enumerate(nums):
            if ele in nums_dict and ind != nums_dict[ele]:
                return [ind, nums_dict[ele]]

        return []

    @staticmethod
    def two_sum_sol2(nums: List[int], target: int) -> List[int]:

        nums_dict = dict()

        for ind, ele in enumerate(nums):
            other_number = target - ele
            if other_number in nums_dict:
                return [ind, nums_dict[other_number]]

            else:
                nums_dict[other_number] = ind

        return []


def main():
    nums = [2, 7, 11, 15]
    target = 9
    print(f"nums : {','.join([str(ele) for ele in nums])} ; target : {target}")
    print(Solution.two_sum_sol2(nums=nums, target=target))

    nums = [3, 2, 4]
    target = 6
    print(f"nums : {','.join([str(ele) for ele in nums])} ; target : {target}")
    print(Solution.two_sum_sol2(nums=nums, target=target))

    nums = [3, 3, 4, 7]
    target = 6
    print(f"nums : {','.join([str(ele) for ele in nums])} ; target : {target}")
    print(Solution.two_sum_sol2(nums=nums, target=target))


if __name__ == '__main__':
    main()