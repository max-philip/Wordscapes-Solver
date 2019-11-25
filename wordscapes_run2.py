import enchant
import itertools
import time

myDict = enchant.Dict("en_US")


def get_combos(k):
    
    letters = list(k)

    comb_List = []
    
    word_list = []

    for ass in range(4, len(letters)+1):
        comb_List.append([list(x) for x in itertools.permutations(letters, ass)])

    for combs in comb_List:
        for comb in combs:
            word = ''.join(comb)
            if (myDict.check(word) and (word not in word_list)) and (len(word) >= 3) and ("'" not in word):
                word_list.append(word)
            
    return word_list


