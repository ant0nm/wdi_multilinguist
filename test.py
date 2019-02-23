from math_genius import MathGenius
from quote_collector import QuoteCollector
from counter import Counter

# test out the MathGenius class
print("Testing out the MathGenius class:")
mg = MathGenius()
print("*{}*".format(mg.current_lang), mg.report_total([23,45,676,34,5778,4,23,5465]))
print("*{}*".format(mg.current_lang), mg.is_it_Prime(37))
mg.travel_to("India")
print("*{}*".format(mg.current_lang), mg.report_total([6,3,6,68,455,4,467,57,4,534]))
print("*{}*".format(mg.current_lang), mg.floor_of(3.5))
print("*{}*".format(mg.current_lang), mg.is_it_Prime(10))
mg.travel_to("Italy")
print("*{}*".format(mg.current_lang), mg.report_total([324,245,6,343647,686545]))
print("*{}*".format(mg.current_lang), mg.floor_of(35.9))
print("*{}*".format(mg.current_lang), mg.is_it_Prime(7))

# test out the QuoteCollector class
print()
print("Testing out the QuoteCollector class:")
qc = QuoteCollector({"wisdom":["A man is what he thinks about all day long.",
    "If there is no God, everything is permitted.",
    "Everyone thinks of changing the world, but no one thinks of changing himself."],
    "friendship": ["It’s better to have 100 friends that 100 rubles.",
    "One old friend is better than two new ones.",
    "A friend in need is a friend indeed."],
    "love": ["Love is blind.",
    "Respect was invented to cover the empty place where love should be.",
    "To love and be loved is to feel the sun from both sides."]})
print("*{}*".format(qc.current_lang),"*wisdom*" ,qc.share_quote("wisdom"))
qc.travel_to("India")
print("*{}*".format(qc.current_lang), "*friendship*" ,qc.share_quote("friendship"))
qc.travel_to("Spain")
print("*{}*".format(qc.current_lang), "*love*" ,qc.share_quote("love"))
qc.travel_to("UK")
print("*{}*".format(qc.current_lang), "*random*" ,qc.share_quote())

# test out the Counter class
print()
print("Testing out the Counter class:")
print("In the UK:")
c = Counter()
c.count_to(10)
print("In France:")
c.travel_to("France")
c.count_to(10)
print("In Spain:")
c.travel_to("Spain")
c.count_to(10)
