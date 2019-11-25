from wordscapes_run2 import get_combos
import time

t = time.process_time()

f = open("20k_filtered.txt", "r")

all_words = []

for line in f:
    text = line

f.close()


# SPECIFIC TO THE 20K THING LMAO
all_words = text.split("', '")
all_words[0] = all_words[0][1:]
all_words[-1] = all_words[-1][:-2]

print("total root count:", len(all_words))


f = open("words_out.txt", "w")

bigger_list = []

i = 0
j = 0

curr_max = 100

for word in all_words:
    pot_list = get_combos(word)
    if len(pot_list) >= 12:
        bigger_list.append(pot_list)
        j += 1
        if (j > curr_max):
            print('read:', i, 'accepted:', j)
            curr_max += 100
    i+=1

    
print("total accepted:", j)
f.write(str(bigger_list))
f.close()
print('DONE')

elapsed_time = time.process_time() - t
print("\nTIME TAKEN:", elapsed_time, "\n")

