from multilinguist import Multilinguist
from random import choice

class QuoteCollector(Multilinguist):

    def __init__(self, fav_quotes):
        # first call the init method of the parent class - Multilinguist
        super().__init__()
        # then add any additional properties uniqie to the QuoteCollector class
        self.fav_quotes = fav_quotes

    def add_quote(self, quote):
        self.fav_quotes.append(append)

    def share_quote(self):
        quote = choice(self.fav_quotes)
        translated_quote = self.say_in_local_language(quote)
        return translated_quote

qc = QuoteCollector(["A man is what he thinks about all day long.",
    "If there is no God, everything is permitted.",
    "Everyone thinks of changing the world, but no one thinks of changing himself.",
    "he two most powerful warriors are patience and time.",
    "If you want to be happy, be.",
    "There is no greatness where there is no simplicity, goodness and truth."])
