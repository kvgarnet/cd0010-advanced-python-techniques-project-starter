import collections


def count_unique_words(filename='hamlet.txt'):
    cnt = collections.Counter()
    # Extract the data into Python.
    with open(filename) as f:
        for line in f:
            cnt.update(line.split())

    # Calculate the ten most common words.
    for word, count in cnt.most_common(10):
        print(word, count)


if __name__ == '__main__':
    count_unique_words('hamlet.txt')
'''
import collections


def count_unique_words(filename):
    # your code here
    cnt = collections.Counter()
    with open(filename) as f:
        for line in f:
            for word in line.strip().lower().split():
                cnt[word] += 1
    return  cnt


if __name__ == '__main__':
    cnt = count_unique_words('hamlet.txt')
    for k,v in cnt.most_common(10):
        print(k,' ',v)


'''

'''


# Create an empty dictionary
d = dict()

# Open the file in read mode
with open("sample.txt", "r") as text:
# Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()

        # Convert the characters in line to
        # lowercase to avoid case mismatch
        line = line.lower()

        # Split the line into words
        words = line.split(" ")
                        

        # Iterate over each word in line
        for word in words:
            # Check if the word is already in dictionary
            if word in d:
                # Increment count of word by 1
                d[word] = d[word] + 1
            else:
                # Add the word to dictionary with count 1
                d[word] = 1

# Print the contents of dictionary
for key in list(d.keys()):
    print(key, ":", d[key])
'''

'''
d = {}
for word in words:
    d[word] = d.get(word, 0) + 1

'''

'''
Consider the files with punctuation
Sample.txt:

Mango! banana apple pear.
Banana, grapes strawberry.
Apple- pear mango banana.
Kiwi "apple" mango strawberry.

'''

'''
import string

# Open the file in read mode
text = open("sample.txt", "r")

# Create an empty dictionary
d = dict()

# Loop through each line of the file
for line in text:
    # Remove the leading spaces and newline character
    line = line.strip()

    # Convert the characters in line to
    # lowercase to avoid case mismatch
    line = line.lower()

    # Remove the punctuation marks from the line
    line = line.translate(line.maketrans("", "", string.punctuation))

    # Split the line into words
    words = line.split(" ")

    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1

# Print the contents of dictionary
for key in list(d.keys()):
    print(key, " ", d[key])

'''
