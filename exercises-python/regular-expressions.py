import re

patterns = ['term1', 'term2']
text = 'This is a string with term1, but not the other term'

re.search('hello', 'hello world!')

for pattern in patterns:
    print ('Searching for: "%s" in: \n"%s"') % (pattern, text),

    #Check for Match
    if re.search(pattern, text):
        print('\n')
        print("Match was found. \n")
    else:
        print('\n')
        print('No match was found.\n')

match = re.search(patterns[0], text)
type(match)
match.start()
match.end()

split_term  = '@'
phrase = 'What is yout email, is it hello@gmail.com?'

re.split(split_term, phrase)

