
def findCharacters(word_list,char):
    new_list = []
    for word in word_list:
        for letter in word:
            if letter==char:
                new_list.append(word)

    print new_list

findCharacters()

