"""
unjumble.py
Find solutions to an anagram puzzle given a dictionary of valid words

2022-09-27 by Alex JPS
"""

# Switch between short test dict and full English dict
DICT_NAME = "dict.txt"
# DICT_NAME = "shortdict.txt"

def normalize(word: str) -> list[str]:
	# Returns canonical (alphabetized) list of characters for input
	"""
	>>> normalize("gamma") == normalize("magam")
	True

	>>> normalize("MAGAM") == normalize("gamma")
	True

	>>> normalize("KAWEA") == normalize("awake")
	True

	>>> normalize("KAWEA") == normalize("gamma")
	False
	"""
	return sorted(word.lower())

def find(canon_anagram: str):
	# Returns list of words in dict matching given normalized anagram
	"""
	>>> find(['a', 'e', 'g', 'm', 'o'])
	['omega']

	>>> find(['a', 'a', 'h', 'l', 'p'])
	['alpha']

	>>> find(['a', 'b', 'e', 't'])
	['abet', 'bate', 'beat', 'beta']
	"""
	matches = []
	dict_file = open(DICT_NAME, "r")

	for line in dict_file:
		word = line.strip()
		if normalize(word) == canon_anagram:
			matches.append(word)
	return matches

def main():
	anagram = input("Input jumbled word: ")

	# Store normalized form to compare dictionary words against
	canon_anagram = normalize(anagram)
	result = find(canon_anagram)

	# Display results
	if len(result) == 0:
		print("No match found! (try a different dictionary?)")
	elif len(result) == 1:
		print(result[0])
	else:
		print("Multiple matches found:")
		for i in result:
			print(i)

if __name__ == "__main__":
	main()
	# Uncomment to run test cases on startup
	# import doctest
	# doctest.testmod()
	# print("Doctests complete!")
