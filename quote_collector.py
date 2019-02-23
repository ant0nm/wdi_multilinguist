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

    def share_quote(self, topic="random"):
        translated_quote = None

        if topic == "random":
            random_key = choice(list(self.fav_quotes.keys()))
            random_quotes = self.fav_quotes[random_key]
            quote = choice(random_quotes)
        else:
            random_quotes = self.fav_quotes[topic]
            quote = choice(random_quotes)

        return self.say_in_local_language(quote)
