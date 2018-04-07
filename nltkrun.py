import nltk
from nltk.stem.lancaster import LancasterStemmer
# word stemmer
stemmer = LancasterStemmer()

training_data = []
training_data.append({"class":"work", "sentence":"Meeting at 2 PM"})
training_data.append({"class":"work", "sentence":"Come to work early"})
training_data.append({"class":"work", "sentence":"Project starts from 10 AM"})
training_data.append({"class":"work", "sentence":"Client issue not solved"})

training_data.append({"class":"home", "sentence":"Son failed at school"})
training_data.append({"class":"home", "sentence":"Bring vegetables while coming back"})
training_data.append({"class":"home", "sentence":"in laws coming today"})
training_data.append({"class":"home", "sentence":"my parents are ill"})
training_data.append({"class":"home", "sentence":"family problems father is ill"})


#
#training_data.append({"class":"spam", "sentence":"buy a credit card"})
#training_data.append({"class":"spam", "sentence":"can you m"})
#training_data.append({"class":"spam", "sentence":"having a spam today?"})
#training_data.append({"class":"spam", "sentence":"what's for lunch?"})
#print ("%s sentences of training data" % len(training_data))

# capture unique stemmed words in the training corpus
corpus_words = {}
class_words = {}
# turn a list into a set (of unique items) and then a list again (this removes duplicates)
classes = list(set([a['class'] for a in training_data]))
for c in classes:
    # prepare a list of words within each class
    class_words[c] = []

# loop through each sentence in our training data
for data in training_data:
    # tokenize each sentence into words
    for word in nltk.word_tokenize(data['sentence']):
        # ignore a some things
        if word not in ["?", "'s"]:
            # stem and lowercase each word
            stemmed_word = stemmer.stem(word.lower())
            # have we not seen this word already?
            if stemmed_word not in corpus_words:
                corpus_words[stemmed_word] = 1
            else:
                corpus_words[stemmed_word] += 1
  # add the word to our words in class list
            class_words[data['class']].extend([stemmed_word])


# we now have each stemmed word and the number of occurances of the word in our training corpus (the word's commonality)
#print ("Corpus words and counts: %s \n" % corpus_words)
# also we have all words in each class
#print ("Class words: %s" % class_words)

def calculate_class_score(sentence, class_name, show_details=True):
    score = 0
    # tokenize each word in our new sentence
    for word in nltk.word_tokenize(sentence):
        # check to see if the stem of the word is in any of our classes
        if stemmer.stem(word.lower()) in class_words[class_name]:
            # treat each word with same weight
            score += 1

            if show_details:
                print ("   match: %s" % stemmer.stem(word.lower() ))
    return score

def calculate_class_score_commonality(sentence, class_name, show_details=True):
    score = 0
    # tokenize each word in our new sentence
    for word in nltk.word_tokenize(sentence):
        # check to see if the stem of the word is in any of our classes
        if stemmer.stem(word.lower()) in class_words[class_name]:
            # treat each word with relative weight
            score += (1 / corpus_words[stemmer.stem(word.lower())])

            if show_details:
                print ("   match: %s (%s)" % (stemmer.stem(word.lower()), 1 / corpus_words[stemmer.stem(word.lower())]))
    return score

def classify(sentence):
    high_class = None
    high_score = 0
    # loop through our classes
    for c in class_words.keys():
        # calculate score of sentence for each class
        score = calculate_class_score_commonality(sentence, c, show_details=False)
        # keep track of highest score
        if score > high_score:
            high_class = c
            high_score = score

    return high_class, high_score


print (classify("family issue"))
