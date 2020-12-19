
def getDictionary():
    openDictionary = open('dictionary.txt','r');
    dictionary = openDictionary.read().split()
    openDictionary.close()
    return dictionary

myword = input("Please enter a word to check:").lower()

dictionary = getDictionary()
if myword in dictionary:
    print(myword, "is a word in the dictionary")
else:
    print(myword, " is not a word in the dictionary")    