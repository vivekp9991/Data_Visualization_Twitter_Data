import csv
import re
import nltk



def cleaning():
    counter = 0

    with open("alldata.csv", "r") as csvfile:
        myfile = csv.reader(csvfile)
        for line in myfile:
            tweet = line[1]
            # 1Removing puncuation.
            tweet= re.sub(r'[^\w\s]','',tweet) #remove punctuation

            # removing customized punctation
            item =re.sub(r"(?:\@|'|https?\://)\s+","",tweet)

            # 2 removing numbers
            tweet=re.sub("\d+","",tweet) # remove number from text

            # tokenization
            token_text = nltk.word_tokenize(tweet)
            # stop word removal
            stopwords = nltk.corpus.stopwords.words('english')  # stopword reduction

            # converting to lower case
            token_text= [w.lower() for w in token_text]

            #
            with open("Cleaned_datacrypto.csv","ab")as csvfile:
                myfile =csv.writer(csvfile)
                myfile.writerow([line[0],token_text,line[2],line[3]])

                counter = counter+1

            print (tweet)
            print ("_______________")

def main():


    cleaning()



main()