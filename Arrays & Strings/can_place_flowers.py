from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return False

        n_planted = 0
        flowerbed = [0] + flowerbed + [0]
        for ind in range(1, len(flowerbed) - 1):
            prev = flowerbed[ind - 1]
            current = flowerbed[ind]
            _next = flowerbed[ind + 1]

            valid_position = all([prev != 1, current != 1, _next != 1])
            if valid_position:
                flowerbed[ind] = 1
                n_planted += 1

            if n_planted == n:
                return True

        return False


def main():
    soln = Solution()

    flowerbed = [1, 0, 0, 0, 1, 0, 0]
    n = 2
    print(soln.canPlaceFlowers(flowerbed=flowerbed, n=n))


if __name__ == '__main__':
    main()
