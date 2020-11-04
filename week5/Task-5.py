ef find(word,letter,index):
    while index<len(word):
        if word[index]==letter:
            return index
        index+=index
        return -1
print(find('westminster','i',0))

