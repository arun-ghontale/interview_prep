from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_array = []
        for val in arr[::-1]:
            if len(max_array) == 0:
                max_array.append(val)

            elif val > max_array[-1]:
                max_array.append(val)

            else:
                max_array.append(max_array[-1])

        max_array = max_array[::-1][1:] + [-1]
        return max_array


def main():
    arr = [17, 18, 5, 4, 6, 1]
    soln = Solution()
    print(soln.replaceElements(arr=arr))

    arr = [1, 32, 72, 11, 56, 13, 29, 1, 3]
    soln = Solution()
    print(soln.replaceElements(arr=arr))


if __name__ == '__main__':
    main()
