import json
def parse_content(content):
    '''
    The parse_content function should accept the text contents of a file 
    return a dictionary mapping a word to its frequency.
    Let's take a look at an example. Suppose that we have the content:

ban     10
band    5
bar     14
can     32
candy   7
This content arrives at the parse_content function as the string "ban 10\nband 5\nbar 14\ncan 32\ncandy 7".

The parse_content function can return anything, but we suggest a dictionary mapping words to their (integer) frequencies. In this case, the parse_content function might return the following dictionary:

{
  'ban': 10,
  'band': 5,
  'bar': 14,
  'can': 32,
  'candy': 7
}
    '''
    word_dict = dict()
    for line in content.split('\n'):
        word,freq = line.split()
        word_dict[word] = int(freq)

    return word_dict

content = "ban 10\nband 5\nbar 14\ncan 32\ncandy 7"
rd= parse_content(content)
# print(rd)
print(json.dumps(rd, indent=4))



def build_trie_from_string(data_string: str) -> dict:
    """
    Parses a string of 'word value' pairs (separated by newlines) and 
    constructs a nested dictionary (Trie) where each key is a character 
    in the word. The final value is stored under a special key 
    in the format "$[word]".

    Args:
        data_string: A multi-line string containing word and value pairs, 
                     e.g., "ban 10\nband 5".

    Returns:
        A dictionary representing the Trie structure.
    """
    trie = {}

    # 1. Process the input string line by line
    for line in data_string.strip().split('\n'):
        # Skip empty lines
        if not line:
            continue

        # Split the line into the word and its corresponding value string
        parts = line.split()
        if len(parts) != 2:
            print(f"Skipping malformed line: '{line}'")
            continue

        word, value_str = parts
        
        try:
            # Convert the value to an integer
            value = int(value_str)
        except ValueError:
            print(f"Skipping line with invalid value: '{line}'")
            continue

        # 2. Traverse or build the Trie path
        current_node = trie
        for char in word:
            # If the character key doesn't exist, create a new empty dictionary
            if char not in current_node:
                current_node[char] = {}
            # Move down to the newly created or existing node
            current_node = current_node[char]
            
        # 3. Mark the end of the word and store the value
        # The termination key uses the format "$[word]" as requested.
        end_key = f"${word}"
        current_node[end_key] = value

    return trie

# Input data provided in the user's request
input_data = "ban 10\nband 5\nbar 14\ncan 32\ncandy 7"

# Build the Trie
result_trie = build_trie_from_string(input_data)

# Print the resulting structure nicely formatted
print("--- Input Data ---")
print(input_data)
print("\n--- Output Trie Structure ---")
# Use json.dumps for pretty printing the nested dictionary
print(json.dumps(result_trie, indent=4))

def predict(tree, numbers):
    '''
Finally, this trie will be provided to the predict function, along with a collection of numbers represented in text, 
as entered by the user - perhaps "2263". In this case, because both "band" and "candy" start with the letters from "2263," 
and none of the other words do, the predict function will return the ordered collection:

[
    ('candy', 7)
    ('band', 5)
]

In a pseudo-code descriptive language, we are indeed performing the following algorithm:

# 1. Find the internal nodes corresponding to the user's supplied letters.
# 2. Build a collection of all of the words that could be built starting from any of those internal nodes.
# 3. Sort the possible words by their frequency.

    '''
