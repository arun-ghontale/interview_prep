from typing import List


class Solution:
    @staticmethod
    def contains_duplicate(nums: List[int], memory_efficient=False) -> bool:

        # O(nlogn) time with O(1) space
        if memory_efficient:
            nums = sorted(nums)
            for ind in range(1, len(nums)):
                prev_ele = nums[ind - 1]
                current_ele = nums[ind]
                if prev_ele == current_ele:
                    return True

            return False

        # O(n) time with O(n) space
        else:
            nums_dict = dict()
            for n in nums:
                if n not in nums_dict:
                    nums_dict[n] = 0

                nums_dict[n] += 1
                if nums_dict[n] > 1:
                    return True

            return False


def main():
    # Test case 1
    nums = [1, 2, 3, 1]
    print(f"nums : {','.join([str(ele) for ele in nums])}; memory_efficient=False")
    print(Solution.contains_duplicate(nums=nums))
    print("\n")

    # Test case 2
    nums = [1, 2, 3, 1]
    print(f"nums : {','.join([str(ele) for ele in nums])}; memory_efficient=True")
    print(Solution.contains_duplicate(nums=nums, memory_efficient=True))
    print("\n")

    # Test case 3
    nums = [1, 2, 3, 4]
    print(f"nums : {','.join([str(ele) for ele in nums])}; memory_efficient=False")
    print(Solution.contains_duplicate(nums=nums))
    print("\n")

    # Test case 4
    nums = [1, 2, 3, 4]
    print(f"nums : {','.join([str(ele) for ele in nums])}; memory_efficient=True")
    print(Solution.contains_duplicate(nums=nums, memory_efficient=True))
    print("\n")

    # Test case 5
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"nums : {','.join([str(ele) for ele in nums])}; memory_efficient=False")
    print(Solution.contains_duplicate(nums=nums))
    print("\n")

    # Test case 6
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"nums : {','.join([str(ele) for ele in nums])}; memory_efficient=True")
    print(Solution.contains_duplicate(nums=nums, memory_efficient=True))
    print("\n")


if __name__ == '__main__':
    main()
