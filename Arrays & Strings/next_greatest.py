from typing import List


class Solution:
    def get_next_greatest(self, start, end, arr, current):
        for ind in range(start, end):
            if arr[ind] > current:
                return arr[ind]

        return -1

    def nextGreaterElementSlow(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = dict()

        for ind in range(0, len(nums2)-1):
            current = nums2[ind]
            next_greatest = self.get_next_greatest(start=ind+1, end=len(nums2), arr=nums2, current=current)
            next_greater[current] = next_greatest

        next_greater[nums2[-1]] = -1

        return [next_greater[n] for n in nums1]

    def pop_stack(self, stack, mapping, num):
        ind = len(stack)
        while ind > 0:
            if stack[-1] < num:
                top = stack.pop()
                mapping[top] = num
            else:
                break

            ind -= 1

        stack.append(num)

    def nextGreaterElementFast(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = list()
        mapping = dict()

        for num in nums2:
            if len(stack) == 0:
                stack.append(num)

            else:
                if stack[-1] < num:
                    self.pop_stack(stack, mapping, num)

                else:
                    stack.append(num)

        for num in stack:
            mapping[num] = -1

        print(mapping)
        return [mapping[num] for num in nums1]


def main():
    soln = Solution()

    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    print(soln.nextGreaterElementFast(nums1, nums2))

    nums1 = [5, 7, 1, 3, 2, 6, 11, 4]
    nums2 = [1, 3, 5, 7, 8, 6, 4, 2, 11]
    print(soln.nextGreaterElementFast(nums1, nums2))

    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    print(soln.nextGreaterElementSlow(nums1, nums2))

    nums1 = [5, 7, 1, 3, 2, 6, 11, 4]
    nums2 = [1, 3, 5, 7, 8, 6, 4, 2, 11]
    print(soln.nextGreaterElementSlow(nums1, nums2))


if __name__ == '__main__':
    main()
