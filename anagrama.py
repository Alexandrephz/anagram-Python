import random

class Word:
    def __init__(self, word):
        self.word = word

    @property
    def word(self):
        return self.__word
    
    @word.setter
    def word(self, new_word):
        if isinstance(new_word, str):
            if len(new_word) > 1:
                self.__word = new_word
            else:
                raise ValueError("Value cannot be null or have 1 digit !")
        else:
            raise TypeError("Wrong type !")

    def word_size(self):
        word_size = len(self.__word)
        return word_size

class ShuffleWord(Word):
    def __init__(self, word):
        super().__init__(word)

    def fatorial_number(self):
        self.fatorial = 1
        for x in range(super().word_size(),1,-1):
            self.fatorial *= x
        return self.fatorial
    
    def duplicated_exclusion(self):
        duplicated_word = {}
        self.fatorial_exclude = 1
        for x in self.word:
            if self.word.count(x) > 1:
                duplicated_word[x] = self.word.count(x)
        for value in duplicated_word:
            self.fatorial_exclude *= duplicated_word[value]
        return self.fatorial_exclude
        

    def possibility_calculator(self):
        anagram_list = []
        anagram_list.append(self.word)
        anagram_size = (self.fatorial_number() / self.duplicated_exclusion()) - 1
        while anagram_size != 0:
            shuffle = ''.join(random.sample(self.word, len(self.word)))
            if not shuffle in anagram_list:
                anagram_list.append(shuffle)
                anagram_size -= 1
            else:
                continue

        return anagram_list

if __name__ == "__main__":
    print("Input:")
    anagram_word = input()
    initialize = ShuffleWord(anagram_word)
    retrieve_list = initialize.possibility_calculator()
    print(retrieve_list)
