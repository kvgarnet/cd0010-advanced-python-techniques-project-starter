def find(letters,words):
    lookup = []
    sorted_letter = ''.join(sorted(letters))
    for word in words:
        key = ''.join(sorted(word))
        if sorted_letter == key:
            lookup.append(word)
    return lookup

result = find("arm", {"mar", "mat", "ram"})  #['ram', 'mar']
print(result)


# use dictionary of set

def find_anagrams(letters, words):
    # Create a dictionary mapping the canonical representation of a word to all anagrams of those letters.
    lookup = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in lookup:
            lookup[key] = set()
        lookup[key].add(word)

    # Search the lookup table for the queried letters.
    search = ''.join((sorted(letters)))
    return lookup.get(search, set())


result = find_anagrams("arm", {"mar", "mat", "ram"})  #['ram', 'mar']
print(result)


# use collections.defaultdict
from collections import defaultdict

def find_anagrams(letters, words):
    lookup = defaultdict(set, {})  # Create a dictionary subclass that adds sets for missing values.
    for word in words:
        lookup[''.join(sorted(word))].add(word)
    return lookup.get(''.join(sorted(letters)), set())


from collections import defaultdict

def find_anagrams(letters, words):
    """
    Finds all anagrams of a given set of letters within a list of words.
    
    This function uses a defaultdict(set) for efficient grouping.
    """
    
    # Simplified initialization: Functionally identical to defaultdict(set, {})
    lookup = defaultdict(set)
    
    # 1. Build the lookup table: Map sorted word to the set of original words
    for word in words:
        # Sort the word to create the canonical key (e.g., "tale" -> "aelt")
        key = ''.join(sorted(word))
        
        # If 'key' doesn't exist, lookup[key] is automatically initialized to set().
        # Then, the original 'word' is added to that set.
        lookup[key].add(word)

    # 2. Get the canonical key for the target letters
    target_key = ''.join(sorted(letters))
    
    # 3. Retrieve the anagrams for the target key.
    # .get() is used here to safely return an empty set if the target_key is not found,
    # without accidentally adding the missing key to the dictionary (a key difference 
    # when reading vs. writing to a defaultdict).
    return lookup.get(target_key, set())

# --- Example Usage ---
word_list = ["listen", "silent", "enlist", "banana", "cat"]
target_letters = "sintle"

anagrams = find_anagrams(target_letters, word_list)

print(f"Word List: {word_list}")
print(f"Target Letters: '{target_letters}'")
print(f"Found Anagrams: {anagrams}")
