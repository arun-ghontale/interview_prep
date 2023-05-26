class Solution:
    def clean_string(self, s: str) -> str:
        s_cleaned = ""
        for c in s:
            if c.isalnum():
                s_cleaned += c.lower()

        return s_cleaned

    def isPalindrome(self, s: str) -> bool:
        s_cleaned = self.clean_string(s)
        print(s_cleaned)
        if len(s_cleaned) == 0:
            return True

        ind_for = 0
        ind_back = len(s_cleaned) - 1

        while ind_for <= ind_back:
            if s_cleaned[ind_for] != s_cleaned[ind_back]:
                return False

            ind_for += 1
            ind_back -= 1

        return True


def main():
    soln = Solution()

    s = "A man, a plan, a canal: Panama"
    print(soln.isPalindrome(s))


if __name__ == '__main__':
    main()