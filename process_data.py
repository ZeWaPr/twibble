import csv

data = open("readed.csv", "r")
tweets = []

for twit in data:
	tweets.append(str(twit).strip())

# print tweets

