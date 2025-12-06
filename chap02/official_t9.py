import json
def parse_content(content):
    words = {}
    for line in content.split('\n'):
        word, frequency = line.split()
        words[word] = int(frequency)
    return words


def make_tree(words):
    trie = {}
    for word, frequency in words.items():
        node = trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node[f'${word}'] = frequency
    return trie



content = "ban 10\nband 5\nbar 14\ncan 32\ncandy 7"
words = parse_content(content)
trie = make_tree(words)

print(json.dumps(trie, indent=4))


'''
This code snippet implements a predictive text function—similar to how old phone keypads (T9) or modern smartphone dialers suggest words based on the numbers you press. It works by traversing the Trie structure you built previously in trie_builder.py.

The overall goal is to take a sequence of digits (e.g., 263) and return a list of matching words (like "and," "ant," "antelope") sorted by a relevance score (the value you stored in the Trie).

'''

import operator

def predict(tree, numbers):
    leaves = [tree]
    for number in numbers:
        leaves = [leaf[letter] for letter in keymap[number] for leaf in leaves if letter in leaf]

    words = {}
    for node in leaves:
        words.update(get_leaves(node))

    return sorted(words.items(), key=operator.itemgetter(1), reverse=True)

def get_leaves(node):
    """Get "leaf" nodes from an internal node – a leaf node starts with '$' and has an integer value."""
    leaves = {}
    for label, child in node.items():
        if not isinstance(child, dict):  # We found a word!
            leaves[label[1:]] = child  # Strip the leading '$'
            continue
        leaves.update(get_leaves(child))  # Recurse on the children.
    return leaves
