from typing import List


class Solution:
    def get_current_row(self, previous_row: List[int]) -> List[int]:
        current_row = [1]
        for ind in range(0, len(previous_row) - 1):
            current_row.append(previous_row[ind] + previous_row[ind+1])

        current_row.append(1)

        return current_row

    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        output.append([1])
        if numRows == 1:
            return output

        output.append([1, 1])
        if numRows == 2:
            return output

        for _ in range(numRows - 2):
            current_row = self.get_current_row(output[-1])
            output.append(current_row)

        return output


def main():
    soln = Solution()
    numRows = 6
    print(soln.generate(numRows=numRows))


if __name__ == '__main__':
    main()
