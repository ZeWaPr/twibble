import csv

data = open("readed.csv", "r")
tweets = []

for twit in data:
	tweets.append(str(twit).strip())

# print tweets

def findWord(w):
  if (re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search == None):
    return True
  else:
    return False

def tweetListHappy():
 happyArray = []
 for i in tweets:
   # tweetlist = i.split()
   if 'happy' in tweetlist:
     happyArray.append(1)
   else:
     happyArray.append(0)
 return happyArray
 
# This is identical to tweetListHappy(), except the function evaluates whether each tweet contains the word "sad" or not.  
def tweetListSad():
 sadArray = []
 for i in tweets:
   tweetlist = i.split()
   if 'sad' in tweetlist:
     sadArray.append(1)
   else: 
     sadArray.append(0)
 return sadArray

# This is identical to tweetListHappy(), except the function evaluates whether each tweet contains the word "angry" or not.   
def tweetListAngry():
 angryArray = []
 for i in tweets:
   tweetlist = i.split()
   if 'angry' in tweetlist:
     angryArray.append(1)
   else:
     angryArray.append(0)
 return angryArray

# This function adds the values of the indices in tweetListHappy() and returns the number of tweets containing the word "happy".
def sumHappy():
  happyArray = tweetListHappy()
  sumHappy = 0
  for i in happyArray:
    sumHappy = sumHappy + i
  return sumHappy

# This function adds the values of the indices in tweetListSad() and returns the number of tweets containing the word "sad".
def sumSad():
  sadArray = tweetListSad()
  sumSad = 0
  for i in sadArray:
    sumSad = sumSad + i
  return sumSad

# This function adds the values of the indices in tweetListAngry() and returns the number of tweets containing the word "angry".
def sumAngry():
  angryArray = tweetListAngry()
  sumAngry = 0
  for i in angryArray:
    sumAngry = sumAngry + i
  return sumAngry 

# This function prints lists describing how many "happy", "sad", and "angry" tweets were present in the data set.  A tweet may be counted in one, two, or all three lists, 
# or in no lists.  Each tweet is only counted once per list type. 
def emotionsCountList():
  happy = sumHappy()
  sad = sumSad()
  angry = sumAngry()
  print "Number of happy tweets: " + str(happy)
  print "Number of sad tweets: " + str(sad)
  print "Number of angry tweets: " + str(angry)