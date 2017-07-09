#Write a function called word_lengths, which takes in one
#parameter, a string, and returns a dictionary where each
#word of the string is mapped to an integer representing how
#how long that word is. You should ignore punctuation, and
#all the words should be lowercase. You can assume that the
#only punctuation marks in the string will be periods,
#commas, question marks, exclamation points, and apostrophes.
#
#For example:
#  word_lengths("I ate a bowl of cereal out of a dog bowl today.")
#  -> {'i':1, 'bowl':4, 'today':5, 'out':3, 'dog':3, 'ate':3,
#      'a':1, 'of':2, 'cereal':6}
#
#Hint: Use the split() method to split by spaces, and don't
#forget to remove punctuation marks.  Remember also: strings
#are immutable, so operations like my_string.lower() don't
#change the value of my_string like list methods: to save
#those results, you'd write my_string = my_string.lower().
#
#Your dictionary should not have any duplicate keys (in fact,
#Python won't allow a dictionary to have duplicate keys).


#Write your function here!
def word_lengths(aString):
    aString = aString.replace(",", "")
    aString = aString.replace(".", "")
    aString = aString.replace("?", "")
    aString = aString.replace("!", "")
    aString = aString.replace("'", "")
    aString = aString.lower()

    words = {}
    for word in aString.split():
        if not word in words:
            words[word] = 0
        words[word] = len(word)

    return words



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#{'dog': 3, 'today': 5, 'of': 2, 'ate': 3, 'bowl': 4, 'out': 3, 'a': 1, 'cereal': 6, 'i': 1}
#
#The order of the keys may differ, but that's okay!
print(word_lengths("I ate a bowl of cereal out of a dog bowl today.") ==
      {'dog': 3, 'today': 5, 'of': 2, 'ate': 3, 'bowl': 4, 'out': 3, 'a': 1, 'cereal': 6, 'i': 1}
)

#print(word_lengths("I ate a bowl of cereal out of a dog bowl today."))


