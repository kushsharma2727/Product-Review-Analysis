import csv, random
import nltk
import tweet_features, tweet_pca


from replacer import *

def int2word(n):
    
    n3 = []
    r1 = ""
    ns = str(n)
    for k in range(3, 33, 3):
        r = ns[-k:]
        q = len(ns) - k
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
    
    nw = ""
    for i, x in enumerate(n3):
        b1 = x % 10
        b2 = (x % 100)//10
        b3 = (x % 1000)//100
        if x == 0:
            continue  
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
    n = 234
    


##############################################################33

def punct( text ):
    puncts='.?!'
    for sym in puncts:
        text= text.replace(sym,' ')
    return abbrvtn(text);

def abbrvtn( text3 ):
    abbrevs={'usa':'United States','gb':'Great Britain'}
    for abbrev in abbrevs:
        text3= text3.replace(abbrev,abbrevs[abbrev])
    return stopwords(text3)

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








#############################################################33

fp = open( 'sentiment.csv', 'rb' )
reader = csv.reader( fp, delimiter=',', quotechar='"', escapechar='\\' )
tweets = []
for row in reader:
    tweets.append( [row[3], row[1]] );


for t in tweets:
    if t[1] == 'irrelevant':
        t[1] = 'neutral'


random.shuffle( tweets );

fvecs = [(tweet_features.make_tweet_dict(t),s) for (t,s) in tweets]
v_train = fvecs[:5]
v_test  = fvecs[5:]



classifier = nltk.NaiveBayesClassifier.train(v_train);


print ('\nAccuracy %f\n' % nltk.classify.accuracy(classifier, v_test))
input1 = raw_input("Please write a sentence to be tested for sentiment. If you type 'exit', the program will quit:\n")
input2 = raw_input("Please write a sentiment\n")
input1.lower()
input1=punct(input1.lower())
print (input1)
input = []
input.append([input1,input2])


result=[(tweet_features.make_tweet_dict(t),s) for (t,s) in input]

test_truth   = [s for (t,s) in v_test]
test_predict = [classifier.classify(t) for (t,s) in result]
print (test_predict)

test_predict2 = [classifier.classify(t) for (t,s) in v_test]


print ('Confusion Matrix')
print (nltk.ConfusionMatrix( test_truth, test_predict2 ))
