
'''
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

'''


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq_word1 = Counter(word1)
        freq_word2 = Counter(word2)
        sorted_word1 = sorted(freq_word1.values())
        sorted_word2 = sorted(freq_word2.values())

        keys_match = set(freq_word1.keys()) == set(freq_word2.keys())
        return sorted_word1 == sorted_word2 and keys_match