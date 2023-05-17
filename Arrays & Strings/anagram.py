from typing import Dict


class Solution:
    @staticmethod
    def get_count_dict(string: str) -> Dict[str, int]:
        count_dict = dict()
        for char in string:
            if char not in count_dict:
                count_dict[char] = 0

            count_dict[char] += 1

        # return count_dict
        return count_dict

    def is_anagram(self, s: str, t: str) -> bool:
        s_dict = self.get_count_dict(string=s)
        t_dict = self.get_count_dict(string=t)

        return True if s_dict == t_dict else False


def main():
    s = 'anagram'
    t = 'nagaram'
    soln = Solution()
    print(f"s : {s}; t : {t} ; is_anagram : {soln.is_anagram(s=s, t=t)}")

    s = 'cat'
    t = 'tar'
    soln = Solution()
    print(f"s : {s}; t : {t} ; is_anagram : {soln.is_anagram(s=s, t=t)}")


if __name__ == '__main__':
    main()