'''
This code snippet implements a predictive text function—similar to how old phone keypads (T9) or modern smartphone dialers suggest words based on the numbers you press. It works by traversing the Trie structure you built previously in trie_builder.py.

The overall goal is to take a sequence of digits (e.g., 263) and return a list of matching words (like "and," "ant," "antelope") sorted by a relevance score (the value you stored in the Trie).
'''
import operator
import json

# --- 1. Keymap for Phone Keypad (Necessary for prediction) ---
keymap = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

# --- 2. Trie Construction Function (from trie_builder.py) ---

def build_trie_from_string(data_string: str) -> dict:
    """
    Parses a string of 'word value' pairs and constructs the Trie structure.
    """
    trie = {}
    for line in data_string.strip().split('\n'):
        if not line: continue
        parts = line.split()
        if len(parts) != 2: continue
        
        word, value_str = parts
        try:
            value = int(value_str)
        except ValueError:
            continue

        current_node = trie
        for char in word:
            if char not in current_node:
                current_node[char] = {}
            current_node = current_node[char]
            
        end_key = f"${word}"
        current_node[end_key] = value
    return trie

# --- 3. Recursive Helper to Find All Words from a Node ---

def get_leaves(node):
    """
    Get "leaf" nodes (complete words and scores) from an internal node.
    A leaf node starts with '$' and has an integer value.
    """
    leaves = {}
    for label, child in node.items():
        # Check if the child value is not a dictionary (i.e., it's the score)
        if not isinstance(child, dict):
            # Strip the leading '$' and store the word and score
            leaves[label[1:]] = child 
            continue
        # Recurse on the children.
        leaves.update(get_leaves(child))
    print(f"leaves: {leaves}")
    return leaves

# --- 4. Main Prediction Function (Trie Traversal) ---

def predict(tree, numbers):
    """
    Predicts words based on a sequence of keypad digits.
    """
    # Start the path at the root of the Trie
    leaves = [tree]
    
    # Traverse the Trie by filtering valid paths for each digit
    for number in numbers:
        if number not in keymap:
            # Handle numbers not in the keymap (e.g., 1 or 0 if not defined)
            print(f"Warning: Digit {number} not in keymap. Stopping prediction.")
            return []

        # List comprehension for efficient traversal and filtering:
        # 1. Iterate over every currently matching 'leaf' node.
        # 2. Iterate over every 'letter' mapped by the current 'number'.
        # 3. If 'letter' is a key in the current 'leaf' node, take the next node (leaf[letter]).
        leaves = [
            leaf[letter] for letter in keymap[number] 
            for leaf in leaves 
            if letter in leaf
        ]
        
        # If no paths match after a digit, stop early
        if not leaves:
            return []

    # Collect all complete words starting from the final set of 'leaves' (nodes)
    words = {}
    for node in leaves:
        words.update(get_leaves(node))

    # Sort the results by score (itemgetter(1)) in reverse (highest score first)
    return sorted(words.items(), key=operator.itemgetter(1), reverse=True)

# --- Example Execution ---

# Build the Trie from your input data
input_data = "ban 10\nband 5\nbar 14\ncan 32\ncandy 7\ncat 50" # Added 'cat 50' for a better example
my_trie = build_trie_from_string(input_data)

print("--- Prediction Examples ---")

# Example 1: Pressing '2' (matches a, b, c)
digits_1 = "2" 
predictions_1 = predict(my_trie, digits_1)
print(f"Digits: '{digits_1}' -> Predictions: {predictions_1}")
# Expected output: All words starting with 'a', 'b', or 'c'

# Example 2: Pressing '226' (matches b-a-n)
# digits_2 = "226" 
# predictions_2 = predict(my_trie, digits_2)
# print(f"Digits: '{digits_2}' -> Predictions: {predictions_2}")
# Expected output: ('can', 32), ('ban', 10), ('band', 5)

# Example 3: Pressing '227' (matches b-a-r)
# digits_3 = "227" 
# predictions_3 = predict(my_trie, digits_3)
# print(f"Digits: '{digits_3}' -> Predictions: {predictions_3}")
# Expected output: ('bar', 14)
