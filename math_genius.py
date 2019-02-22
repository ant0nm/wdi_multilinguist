from multilinguist import Multilinguist

class MathGenius(Multilinguist):

    def report_total(self, numbers):
        translation = self.say_in_local_language("The total is")
        total = sum(numbers)
        return "{} {}".format(translation, total)
