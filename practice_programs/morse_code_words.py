from collections import Counter
def morse_words(words):
    codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",
             ".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    

    transformed_words= [None]*len(words)
    for i in range(len(words)):
        w = words[i]
        transformation = ""
        for j in range(len(w)):
            if transformation == "":
                separator = ""
            else:
                separator = "*"
            transformation = transformation + separator + codes[english_letters.index(w[j])]
        transformed_words[i] = transformation
    return transformed_words

words = ["gin","zen","gig","msg"]
print(morse_words(words))


