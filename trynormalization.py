from replacer import *

def int2word(n):
    """
    convert an integer number n into a string of english words
    """
    # break the number into groups of 3 digits using slicing
    # each group representing hundred, thousand, million, billion, ...
    n3 = []
    r1 = ""
    # create numeric string
    ns = str(n)
    for k in range(3, 33, 3):
        r = ns[-k:]
        q = len(ns) - k
        # break if end of ns has been reached
        if q < -2:
            break
        else:
            if  q >= 0:
                n3.append(int(r[:3]))
            elif q >= -1:
                n3.append(int(r[:2]))
            elif q >= -2:
                n3.append(int(r[:1]))
        r1 = r
    
    #print n3  # test
    
    # break each group of 3 digits into
    # ones, tens/twenties, hundreds
    # and form a string
    nw = ""
    for i, x in enumerate(n3):
        b1 = x % 10
        b2 = (x % 100)//10
        b3 = (x % 1000)//100
        #print b1, b2, b3  # test
        if x == 0:
            continue  # skip
        else:
            t = thousands[i]
        if b2 == 0:
            nw = ones[b1] + t + nw
        elif b2 == 1:
            nw = tens[b1] + t + nw
        elif b2 > 1:
            nw = twenties[b2] + ones[b1] + t + nw
        if b3 > 0:
            nw = ones[b3] + "hundred " + nw
    return nw
############# globals ################
ones = ["", "one ","two ","three ","four ", "five ",
    "six ","seven ","eight ","nine "]
tens = ["ten ","eleven ","twelve ","thirteen ", "fourteen ",
    "fifteen ","sixteen ","seventeen ","eighteen ","nineteen "]
twenties = ["","","twenty ","thirty ","forty ",
    "fifty ","sixty ","seventy ","eighty ","ninety "]
thousands = ["","thousand ","million ", "billion ", "trillion ",
    "quadrillion ", "quintillion ", "sextillion ", "septillion ","octillion ",
    "nonillion ", "decillion ", "undecillion ", "duodecillion ", "tredecillion ",
    "quattuordecillion ", "sexdecillion ", "septendecillion ", "octodecillion ",
    "novemdecillion ", "vigintillion "]
if __name__ == '__main__':
    # select an integer number n for testing or get it from user input
    #n = 4321234567890
    #n = 1111111111111
    #n = 1234567890123
    n = 234
    #n = 1



##############################################################33

# Function definition is here
def punct( text ):
    text.lower()
    puncts='.?!'
    for sym in puncts:
        text= text.replace(sym,' ')
    abbrvtn(text);

def abbrvtn( text3 ):
    abbrevs={'usa':'United States','gb':'Great Britain'}
    for abbrev in abbrevs:
        text3= text3.replace(abbrev,abbrevs[abbrev])
    stopwords(text3)

def stopwords( text4 ):
    replacer = RegexpReplacer()
    result5 = replacer.replace(text4)
    temp_corpus=result5.split(' ')
    stops=['hm','why','not','and','are']
    result4=[token for token in temp_corpus if token not in stops]
    i=0
    for x in result4:
        if x.isdigit():
            y=int2word(result4[i])
            result4[i]=y
            i=i+1
    i=i+1
    res=' '.join(result4)
    return res




