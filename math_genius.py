from multilinguist import Multilinguist
import math

class MathGenius(Multilinguist):

    def report_total(self, numbers):
        total = sum(numbers)
        translation = self.say_in_local_language("The total is {}".format(total))
        return translation

    def floor_of(self, number):
        floor = math.floor(number)
        translation = self.say_in_local_language("The largest integer <= {} is {}".format(number, floor))
        return translation

    def is_Prime(self, number):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    return False
            else:
                return True
        else:
            return False

    def is_it_Prime(self, number):
        isPrime = self.is_Prime(number)
        answer = None
        if isPrime:
            answer = "{} is a prime number.".format(number)
        else:
            answer = "{} is not a prime number.".format(number)
        translated_answer = self.say_in_local_language(answer)
        return translated_answer

# mg = MathGenius()
# # 2 is "ODD" - it's the only even number that is a prime number
# print(mg.isPrime(10))
