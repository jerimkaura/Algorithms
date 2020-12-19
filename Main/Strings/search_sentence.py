paragraph = "This is the very last of us Tacco .We appreciate what Tacco receive.Jerry is a group of saints"
word  = "Tacco"

sen_list = []
sen_list = paragraph.split(".")

sen_with_word = []

for sentence in sen_list:
    if sentence.count(word)>0:
        sen_with_word.append(sentence)
        print(sentence)        