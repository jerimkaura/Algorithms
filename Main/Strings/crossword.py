def getDictionary():
    openDictionary = open('dictionary.txt', 'r')
    dictionary = openDictionary.read().split()
    openDictionary.close()
    return dictionary

def solver(string,dictionary):
    nonBlanks = len(string) - string.count(' ')#finding the number of non-blank spaces
    for word in dictionary:
        letterPosition = 0
        matchCount = 0
        if len (word) == len (string):#only compare words with the same lenght
            for letter in string:
                if letter == word[letterPosition]:
                    matchCount += 1
                letterPosition += 1
            if nonBlanks == matchCount:
                print(word)         
    return  
              
word = input("Input your word, type space where incomplete:")
dictionary = getDictionary()
solver(word,dictionary)
