class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        string_mapping = dict()
        # It is sometimes possible that in the t string we try to map the already existing characters
        already_mapped = set()
        for ind in range(0, len(s)):
            c_s = s[ind]
            c_t = t[ind]
            if c_s not in string_mapping and c_t not in already_mapped:
                string_mapping[c_s] = c_t
                already_mapped.add(c_t)

        for ind in range(0, len(s)):
            c_s = s[ind]
            c_t = t[ind]

            if string_mapping.get(c_s, None) != c_t:
                return False

        return True


def main():
    soln = Solution()
    s = "badc"
    t = "baba"
    print(soln.isIsomorphic(s=s, t=t))


if __name__ == '__main__':
    main()
