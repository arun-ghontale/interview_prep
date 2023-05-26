from collections import Counter


class Solution:
    def count_balloon(self, balloon_mapping: dict) -> int:
        single_letter_min_count = None
        double_letter_min_count = None

        for c, count in balloon_mapping.items():
            if count == 0:
                return 0

            if c in {'b', 'a', 'n'}:
                if single_letter_min_count is None:
                    single_letter_min_count = count
                single_letter_min_count = min(single_letter_min_count, count)

            elif c in {'l', 'o'}:
                if double_letter_min_count is None:
                    double_letter_min_count = count
                double_letter_min_count = min(double_letter_min_count, count)

        return min(single_letter_min_count, double_letter_min_count // 2)

    def maxNumberOfBalloonsSlow(self, text: str) -> int:
        balloon_mapping = {c: 0 for c in 'balloon'}

        for c in text:
            if c in balloon_mapping:
                balloon_mapping[c] += 1

        return self.count_balloon(balloon_mapping)

    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_mapping = Counter('balloon')
        text_mapping = Counter(text)

        return min([text_mapping.get(c, 0) // balloon_mapping.get(c,0) for c in 'balloon'])
