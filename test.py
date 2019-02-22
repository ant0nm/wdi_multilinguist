from math_genius import MathGenius
from quote_collector import QuoteCollector

# test out the MathGenius class
print("Testing out the MathGenius class:")
mg = MathGenius()
print("*{}*".format(mg.current_lang), mg.report_total([23,45,676,34,5778,4,23,5465]))
mg.travel_to("India")
print("*{}*".format(mg.current_lang), mg.report_total([6,3,6,68,455,4,467,57,4,534]))
mg.travel_to("Italy")
print("*{}*".format(mg.current_lang), mg.report_total([324,245,6,343647,686545]))

# test out the QuoteCollector class
print()
print("Testing out the QuoteCollector class:")
qc = QuoteCollector(["A man is what he thinks about all day long.",
    "If there is no God, everything is permitted.",
    "Everyone thinks of changing the world, but no one thinks of changing himself.",
    "he two most powerful warriors are patience and time.",
    "If you want to be happy, be.",
    "There is no greatness where there is no simplicity, goodness and truth."])
print("*{}*".format(qc.current_lang), qc.share_quote())
qc.travel_to("India")
print("*{}*".format(qc.current_lang), qc.share_quote())
qc.travel_to("Spain")
print("*{}*".format(qc.current_lang), qc.share_quote())
qc.travel_to("UK")
print("*{}*".format(qc.current_lang), qc.share_quote())
