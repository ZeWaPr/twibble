import re
import csv

data = open("readed.csv", "r")
tweets = []

for twit in data:
  tweets.append(str(twit).strip())

# print tweets

happySyn = ['happy', 'glad', 'excited', ':)', 'love', ':-))','great', 'lol', 'ecstatic', 'thrilled', ';)', 'gleeful', ':d', 'joyful', 'yay', 'hooray', ':-)', ':o)', '=)', '\o/','xd' ]
sadSyn = ['sad', 'depressed', 'fml', 'worry', 'worried', 'sorry', 'somber', 'crying', 'heartbroken', 'alone', 'bummed', ':(', 'blah', 'meh', 'downer', ':-(', '</3']
angrySyn = ['angry', 'pissed', 'mad', '>:(', 'petulance', '>.<', 'upset', 'furious', 'outraged', 'rage', 'outrage', 'irritated', 'irritable', 'vexed', 'tantrum', 'hissy', 'aggravated', 'annoyed', 'ballistic', 'ticked' ]

# Each individual tweet in a given array is broken into another array made of a list of words contained in that tweet.  Another array is then created for the set of tweets as a
# whole which looks at each individual tweet array and assigns a value of 0 or 1 for that tweet.  A 0 is" assigned if the individual tweet contains a specified word ("happy").
# A 1 is assigned if the tweet does not contain that word.  This is done for all tweets in the original array.  The resulting array is the returned value.  

def tweetListFilter(_tweets, _emotions):
  emotionArray=[]
  for tweet in _tweets:
    tweetlower=tweet.lower()
    wordsintweetlower = re.split('[, | |. |! |\? |\"]',tweetlower)  #splits tweets based on designated characters; '; |, | |. |! |: |\? |\"'
    for i in _emotions: 
      if i in wordsintweetlower: 
        synIndex = wordsintweetlower.index(i)  #gets the indexposition of the syn word in the array of the tweet
        if synIndex > 0:
          before = wordsintweetlower[synIndex - 1]  #get the word in index position of the word before the syn word
          checkNot = before[-3:] #sets variable to last three letters of the word before our syn
          if checkNot == "not":  #  checks if word before syn is "not", or ends in "not";  note:  this ignores a handful of english words that end in "not" (ex. knot).  Determined missing results would be minimal
            emotionArray.append(0)
            break
          elif checkNot == "n't":  # checks if word before syn ends in "n't"
            emotionArray.append(0)
            break
          else:
            emotionArray.append(1) # if syn not preceded by "not" or "n't", then appends 1 to emotionsArray
            break
        else:
          emotionArray.append(1)  # if syn present as first word, then appends 1 to emotionsArray
          break
      else: 
        emotionArray.append(0)  # if syn not present, appends 0 to emotionsArray
  sumEmotion = 0
  for i in emotionArray:  # Counts total number of 1s in emotionsArray to determine total number of applicable tweets for emotion
    sumEmotion += i
  return sumEmotion


# This function prints lists describing how many "happy", "sad", and "angry" tweets were present in the data set.  A tweet may be counted in one, two, or all three lists, 
# or in no lists.  Each tweet is only counted once per list type. 
def display():
  happy = tweetListFilter(tweets, happySyn)
  sad = tweetListFilter(tweets, sadSyn)
  angry = tweetListFilter(tweets, angrySyn)
  print "Number of happy tweets: " + str(happy)
  print "Number of sad tweets: " + str(sad)
  print "Number of angry tweets: " + str(angry) + "\n"
  
  totalCount = happy + sad + angry
  
  happyFraction = float(happy)/float(totalCount)
  sadFraction = float(sad)/float(totalCount)
  angryFraction = float(angry)/float(totalCount)

  print "Happy fraction:" + str(happyFraction)
  print "Sad fraction:" + str(sadFraction)
  print "Angry fraction:" + str(angryFraction) + "\n"

display()