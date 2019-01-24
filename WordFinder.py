import itertools

x = open('/Users/Lincy/Downloads/words.txt', "r")

# arranging all the words into a list

wordlist = x.readlines()
newwordlist = []

# editing to remove whitespace
for words in wordlist:
    word = words[:-2]
    newwordlist.append(word)

print("How many slots are there?:")
slots = int(input())

print("Enter each letter, and hit enter when done:")

letters = str(input())
# letters = 'eakeydnerilx'
letters = letters.replace(" ", "")
letters = letters.replace(",", "")
letters = list(letters)

'''letter_list = []
for letter in range(len(letters)):
    letter_list.append(letters[letter])'''

potential = []

for permutation in list(itertools.permutations(letters, slots)):
    permutation = str(permutation)
    permutation = permutation.replace("(", "")
    permutation = permutation.replace(")", "")
    permutation = permutation.replace(",", "")
    permutation = permutation.replace("'", "")
    permutation = permutation.replace(" ", "")
    if permutation in newwordlist:
        potential.append(permutation)

newpotential = []
for elements in potential:
    if elements in newpotential:
        z = 1
    else:
        newpotential.append(elements)
print(newpotential)
