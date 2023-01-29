import doctest

def is_even(n: int) -> bool:
	"""Returns True if n is even, False otherwise

	Args:
		n: integer number to be checked
	Returns:
		True if n is even
		False otherwise

	>>> is_even(100)
	True
	>>> is_even(101)
	False
	>>> is_even(0)
	True
	"""
	return (n % 2) == 0

def welcome():
	"""Print a welcome message and return None (void)
	
	>>> welcome()
	Good morning, CIS 210!
	"""
	print("Good morning, CIS 210!")
	return None

def main():
	doctest.testmod()
	print("Ran docstring tests")

	welcome()

	# Explicit call print when not running from shell
	print(f"Is 2 even? {is_even(2)}")
	print(f"Is 3 even? {is_even(3)}")

if __name__ == "__main__":
	main()
