#Without Enumarate
index_count = 0
word = 'abcde'

for letter in word:
    print(word[index_count])
    index_count += 1

#With Enumerate
for item in enumerate(word):
    print(item)