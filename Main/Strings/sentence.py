"""This code finds if a given words is in the dictionary supplied"""

def getDictionary():
    openDictionary = open('dictionary.txt','r')
    dictionary = openDictionary.read().split()
    openDictionary.close()
    return dictionary

dictionary = getDictionary()
myword = input("Please enter a word to check:").lower()
if myword in dictionary:
    print(myword, "is a word in the dictionary")
else:
    print(myword, " is not a word in the dictionary")    
