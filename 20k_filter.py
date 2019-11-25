f = open("20k.txt", "r")

sixes = []

for word in f:
    if len(word[:-1]) == 6:
        sixes.append(word[:-1])

f.close()
print(sixes)
g = open("20k_filtered.txt", "w")

g.write(str(sixes))

g.close()


print("DONE")
