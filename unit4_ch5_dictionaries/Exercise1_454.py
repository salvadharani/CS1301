myString = "The quick brown fox jumps over the lazy mad dog."

mySplitString = myString.split()
wordDictionary = {}
for word in mySplitString:
    # if word in wordDictionary:
    if not word in wordDictionary:
        # wordDictionary[word] += 1
        wordDictionary[word] = 0
        #wordDictionary[word] = 1
    wordDictionary[word] += 1
print(wordDictionary)

