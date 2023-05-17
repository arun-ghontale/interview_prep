from typing import List


class Solution:
    def smallest_str_len(self, strs: List[str]) -> int:
        min_len = len(strs[0])
        for string in strs[1:]:
            min_len = min(min_len, len(string))

        return min_len

    def check_if_str_match(self, strs: List[str], ind: int):
        unique_str = set()
        for string in strs:
            unique_str.add(string[ind])

        return True if len(unique_str) == 1 else False

    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""

        smallest_len = self.smallest_str_len(strs=strs)
        ind = 0

        while ind < smallest_len:
            if self.check_if_str_match(strs=strs, ind=ind):
                common_prefix += strs[0][ind]
            else:
                break

            ind += 1

        return common_prefix


def main():
    soln = Solution()

    strs = ["flower", "flow", "flight"]
    print(f"strings : {strs}; longest common prefix : {soln.longestCommonPrefix(strs=strs)}")

    strs = ["dog", "racecar", "car"]
    print(f"strings : {strs}; longest common prefix : {soln.longestCommonPrefix(strs=strs)}")


if __name__ == '__main__':
    main()
