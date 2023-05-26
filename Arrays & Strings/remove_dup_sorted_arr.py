from typing import List


class Solution:
    def move_to_left(self, nums: List[int]) -> int:
        ind = 0
        ind_valid_ele = 0

        while ind < len(nums):
            if nums[ind] != '_':
                nums[ind_valid_ele] = nums[ind]
                ind_valid_ele += 1

            ind += 1

        n_valid = ind_valid_ele

        while ind_valid_ele < len(nums):
            nums[ind_valid_ele] = '_'
            ind_valid_ele += 1

        return n_valid

    def removeDuplicates(self, nums: List[int]) -> int:
        already_present = set()

        ind = 0
        while ind < len(nums):
            if nums[ind] in already_present:
                nums[ind] = '_'
            else:
                already_present.add(nums[ind])

            ind += 1

        n_valid = self.move_to_left(nums=nums)
        return n_valid


def main():
    soln = Solution()

    nums = [1,1,2]
    print(soln.removeDuplicates(nums=nums))

    nums = [0,0,1,1,1,2,2,3,3,4]
    print(soln.removeDuplicates(nums=nums))


if __name__ == '__main__':
    main()