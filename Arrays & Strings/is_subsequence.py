class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # count number of character matches in sequence
        match = 0
        # s should always be less than t
        if len(s) > len(t):
            return False

        ind_s, ind_t = 0, 0
        while ind_s < len(s) and ind_t < len(t):
            if s[ind_s] == t[ind_t]:
                ind_s += 1
                match += 1

            ind_t += 1

        if match == len(s):
            return True

        return False

    def wrong(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)

        # s should always be less than t
        if len_s > len_t:
            return False

        ind_s, ind_t = 0, 0
        while ind_s < len_s and ind_t < len_t:
            if s[ind_s] == t[ind_t]:
                ind_s += 1
                ind_t += 1

            else:
                ind_t += 1

        if ind_s >= (len_s - 1):
            return True

        return False


def main():
    soln = Solution()

    s = "abc"
    t = "ahbgdc"
    print(f"s : {s}; t : {t}; is_subseq : {soln.isSubsequence(s=s, t=t)}")

    s = "axc"
    t = "ahbgdc"
    print(f"s : {s}; t : {t}; is_subseq : {soln.isSubsequence(s=s, t=t)}")

    s = "b"
    t = "c"
    print(f"s : {s}; t : {t}; is_subseq : {soln.wrong(s=s, t=t)}")


if __name__ == '__main__':
    main()
