import re
import csv

data = open("readed.csv", "r")
tweets = []

for twit in data:
  tweets.append(str(twit).strip())

# print tweets

#tweets = ['hello', 'pissed I am', 'I am ;)']

happySyn = ['happy', 'glad', 'excited', ':)', 'love', ':-))','great', 'lol', 'ecstatic', 'thrilled', ';)', 'gleeful', ':d', 'joyful', 'yay', 'hooray', ':-)', ':o)', '=)', '\o/','xd' ]
sadSyn = ['sad', 'depressed', 'fml', 'worry', 'worried', 'sorry', 'somber', 'crying', 'heartbroken', 'alone', 'bummed', ':(', 'blah', 'meh', 'downer', ':-(', '</3']
angrySyn = ['angry', 'pissed', 'mad', '>:(', 'petulance', '>.<', 'upset', 'furious', 'outraged', 'rage', 'outrage', 'irritated', 'irritable', 'vexed', 'tantrum', 'hissy', 'aggravated', 'annoyed', 'ballistic', 'ticked' ]

# Each individual tweet in a given array is broken into another array made of a list of words contained in that tweet.  Another array is then created for the set of tweets as a
# whole which looks at each individual tweet array and assigns a value of 0 or 1 for that tweet.  A 0 is" assigned if the individual tweet contains a specified word ("happy").
# A 1 is assigned if the tweet does not contain that word.  This is done for all tweets in the original array.  The resulting array is the returned value.  

def tweetListFilter(_tweets, _emotions):
  sumEmotion = 0
  for tweet in _tweets:
    tweetlower=tweet.lower()
    #splits tweets based on designated characters; '; |, | |. |! |: |\? |\"'
    wordsintweetlower = re.split('[, | |. |! |\? |\"]',tweetlower)  
    for i in _emotions: 
      if i in wordsintweetlower:
        #gets the index position of the syn word in the array of the tweet
        synIndex = wordsintweetlower.index(i)  
        if synIndex > 0:
          #get the word in index position of the word before the syn word
          before = wordsintweetlower[synIndex - 1]  
          #sets variable to last three letters of the word before our syn
          checkNot = before[-3:] 
          #  checks if word before syn is "not", or ends in "not";  
          #note:  this ignores a handful of english words that end in "not" (ex. knot).  Determined missing results would be minimal
          if checkNot == "not":  
            break
          # checks if word before syn ends in "n't"
          elif checkNot == "n't":  
            break
          else:
            # if syn not preceded by "not" or "n't", then appends 1 to emotionsArray
            sumEmotion = sumEmotion + 1 
            break
        else:
          # if syn present as first word, then appends 1 to emotionsArray
          sumEmotion = sumEmotion + 1  
          break
  return sumEmotion

# This function is used to turn LED lights on for particular corresponding emotions for the emotion(s) w/ largest # of tweets
# Red = angry, Blue = sad, Happy = green
def turnOnLight(_emotionType):
	print _emotionType + "is ON"

# This function displays information gathered from Tweets and uses turnOnLight function to do so
def display():

  # Creates int variables for each emotion.  The value of each variable is equal to the number of tweets reflecting that emotion 
  happy = tweetListFilter(tweets, happySyn)
  sad = tweetListFilter(tweets, sadSyn)
  angry = tweetListFilter(tweets, angrySyn)
  
  # Counts total number of tweets that have specificed emotion words
  totalCount = happy + sad + angry
  
  # !!!!Remember to turn all lights off

  
if totalCount == 0:
	print "No Tweets" 
else:
    print "Number of happy tweets: " + str(happy)
  	print "Number of sad tweets: " + str(sad)
    print "Number of angry tweets: " + str(angry) + "\n"

# Variable that stores an array of happy, sad, and angry tweet numbers
colorVal = [happy, sad, angry]

# Variable used to transmit information to the hardward
ledLightReference = ['Happy', 'Sad', 'Angry']

# maxVal will be used later to keep track of which emotion has the largest value
maxVal = happy

# Assigns variable maxVal to the greatest number in colorVal array.  
#This is the largest number of tweets associated with a particular emotions
i = 1
while (i < 3):
	if int(colorVal[i]) > maxVal:
		maxVal = colorVal[i]
	i = i + 1


# Checks the number of tweets associated with each emotion.
#If the number of tweets is equal to maxVal, turn the lights on for that emotion
j = 0
while (j < 3):
	if int(colorVal[j]) == maxVal:
		turnOnLight(ledLightReference[j])
	j = j + 1

display()