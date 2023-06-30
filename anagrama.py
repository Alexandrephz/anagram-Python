import random
from collections import Counter

class ShuffleWord:
    def __init__(self, word):
        self.word = word
        self.word_size = len(word)
        self.fatorial = 1
        self.duplicated_exclusion = 1

    def calculate_factorial(self, n):
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial

    def calculate_duplicated_exclusion(self):
        letter_counts = Counter(self.word)
        for count in letter_counts.values():
            if count > 1:
                self.duplicated_exclusion *= self.calculate_factorial(count)
        return self.duplicated_exclusion

    def generate_anagrams(self):
        anagram_list = []
        self.generate_anagrams_helper(list(self.word), len(self.word), anagram_list)
        return anagram_list

    def generate_anagrams_helper(self, word_list, n, anagram_list):
        if n == 1:
            anagram = ''.join(word_list)
            anagram_list.append(anagram)
        else:
            for i in range(n):
                word_list[i], word_list[n - 1] = word_list[n - 1], word_list[i]
                self.generate_anagrams_helper(word_list, n - 1, anagram_list)
                word_list[i], word_list[n - 1] = word_list[n - 1], word_list[i]

    def possibility_calculator(self):
        total_anagrams = self.calculate_factorial(self.word_size) // self.calculate_duplicated_exclusion()
        anagram_list = self.generate_anagrams()
        random.shuffle(anagram_list)
        return anagram_list[:total_anagrams]


if __name__ == "__main__":
    print("Input:")
    anagram_word = input()
    initialize = ShuffleWord(anagram_word)
    retrieve_list = initialize.possibility_calculator()
    print(retrieve_list)