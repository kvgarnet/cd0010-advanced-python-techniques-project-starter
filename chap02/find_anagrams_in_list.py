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
