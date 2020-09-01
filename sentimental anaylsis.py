filename = open("project_twitter_data.csv", "r")
result = open("resulting_data.csv", "w")
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(string):
    for punctuation_char in punctuation_chars:
        string = string.replace(punctuation_char, "")
    return string

def get_pos(stri):
    stri = strip_punctuation(stri)
    strin = stri.lower()
    list_strin = strin.split()
    accum = 0 
    for word in list_strin:
        for positive_word in positive_words:
            if word == positive_word:
                accum = accum + 1
    return accum

def get_neg(stri):
    stri = strip_punctuation(stri)
    strin = stri.lower()
    list_strin = strin.split()
    accum = 0 
    for word in list_strin:
        for negative_word in negative_words:
            if word == negative_word:
                accum = accum + 1
    return accum

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
            
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
def analysis(result):
    result.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    result.write("\n")

    lines =  filename.readlines()
    header= lines.pop(0)
    for line in lines:
        list = line.strip().split(',')
        result.write("{}, {}, {}, {}, {}".format(list[1], list[2], get_pos(list[0]), get_neg(list[0]), (get_pos(list[0])-get_neg(list[0]))))    
        result.write("\n")

        

analysis(result)
filename.close()
result.close()
