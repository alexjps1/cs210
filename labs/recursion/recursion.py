def bowtie(length):
	if length > 0:
		print('*' * length)
		bowtie(length - 1)
		print('*' * length)

def check_vowel(letter: str)-> int:
    """
    Returns 1 if given letter is a vowel, 0 otherwise
    """
    if letter.upper() in ['A', 'E', 'I', 'O', 'U']:
        return 1
    return 0

def count_vowels(string: str, letter: int = 0, count: int = 0) -> int:
    """
    Returns count of vowels in the given string

    >>> count_vowels('abc de')
    2
    >>> count_vowels('Hi Everyone!')
    5
    """
    # base case end of string
    if letter == len(string):
        return count
    else:
        return check_vowel(string[letter]) + count_vowels(string, letter + 1, count)

def is_list(a: list) -> bool:
    return isinstance(a, list)

def deep_reverse(a: list) -> list:
    result = []
    for i in reversed(a):
        if is_list(i):
            result.append((deep_reverse(i)))
        else:
            result.append(i)
    return result

def main():
	# bowtie(10)
    print(count_vowels("qwertyuiop"))
    print(deep_reverse([1, 2, [3, [4, 5], 6], 7, 8]))

if __name__ == "__main__":
	main()
