from multilinguist import Multilinguist
from num2words import num2words

class Counter(Multilinguist):

    def count_to(self, number):
        for i in range(1, number+1):
            num_in_words = num2words(i)
            translation = self.say_in_local_language(num_in_words)
            print(translation)
