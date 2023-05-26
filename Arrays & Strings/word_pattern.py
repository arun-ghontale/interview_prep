class Solution:
    def wordPatternAnother(self, pattern: str, s: str) -> bool:
        words_list = s.split()
        if len(pattern) != len(words_list):
            return False

        mapping = dict()
        already_mapped = set()

        for char, word in zip(pattern, words_list):
            # if char not in mapping and the word to be mapped is not already mapped
            # This is to avoid same word getting mapped multiple characters
            # Eg: "abba" and "dog dog dog dog"
            if char not in mapping and word not in already_mapped:
                mapping[char] = word
                already_mapped.add(word)

            # if the mapping for the character can't be found
            elif mapping.get(char, None) != word:
                return False

        return True

    def wordPattern(self, pattern: str, s: str) -> bool:
        words_list = s.split()
        if len(pattern) != len(words_list):
            return False

        word2char = dict()
        char2word = dict()

        for char, word in zip(pattern, words_list):
            if char not in char2word and word not in word2char:
                word2char[word] = char
                char2word[char] = word

            elif char2word.get(char) != word or word2char.get(word) != char:
                return False

        return True

