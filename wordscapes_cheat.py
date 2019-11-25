import enchant
import itertools
import time

myDict = enchant.Dict("en_US")


def print_all(search_dict):

    for letter in set(search_dict.keys()):
        letter_set = set(search_dict[letter])
        print(letter, ":", len(letter_set), "\n")
        print(set(search_dict[letter]),"\n\n")


def regex(search_dict, letters, regex_in):
    reg_inds = []
    i=0
    in_len = len(regex_in)

    search_words = []
    for char in list(regex_in):
        if (char != '?'):
            reg_inds.append((char, i))
        i+=1

    out_words = []
    for letter in letters:
        if (letter in search_dict):
            append_elems(out_words,
                comp_placeholders(search_dict[letter], reg_inds, in_len))
        
    print(out_words)


def append_elems(out_list, new_words):
    for word in new_words:
        if (word not in out_list):
            out_list.append(word)
    return out_list


def comp_placeholders(words, inds, in_len):
    out_words = []
    for word in set(words):
        out_word = ''
        if (len(word) == in_len):
            do_cont = True
            for ind in inds:
                if (word[ind[1]] != ind[0]):
                    do_cont = False

            if (do_cont):
                out_words.append(word)

    return out_words
    

while(1):

    k = input("\nGive me ur letters: ")

    t = time.process_time()

    min_len = int(input("Minimum word length: "))

    letters = list(k)
    print(letters, '\n')

    comb_List = []

    for ass in range(min_len, len(letters)+1):
        comb_List.append([list(x) for x in itertools.permutations(letters, ass)])
        
    search_Dict = {}

    for combs in comb_List:
        for comb in combs:
            word = ''.join(comb)
            if myDict.check(word):
                if word[0] in search_Dict:
                    search_Dict[word[0]].append(word)
                else:
                    search_Dict[word[0]] = [word]

    print_all(search_Dict)

    elapsed_time = time.process_time() - t

    print("\nTIME TAKEN:", elapsed_time, "\n")

    while(1):

        j = input("\n\n[x] to QUIT.\nGive me unknown word w/ placeholders [?]: ")

        if (j == 'x'):
            break
        
        regex(search_Dict, letters, j)

        print("\n")

