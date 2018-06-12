#Case 1
myString = "Guilherme"
for letter in myString:
    if letter == 'h':
        continue
    print(letter)

#Case 2
myString = "Guilherme"
for letter in myString:
    if letter == 'h':
        pass
    print(letter)

#Case 3 
myString = "Guilherme"
for letter in myString:
    if letter == 'h':
        break
    print(letter)


