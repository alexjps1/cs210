"""boggler.py
Boggle game solver

CS 210, Fall 2022
2022-11-07
by Alex JPS
"""
import doctest
import sys
import config
import board_view

# Configuration symbolic constants
MIN_WORD = config.MIN_WORD
BOARD_SIZE = config.BOARD_SIZE
N_ROWS = config.N_ROWS
N_COLS = config.N_COLS

# Possible search outcomes
NOPE = "Nope"       # Not a match, nor a prefix of a match
MATCH = "Match"     # Exact match to a valid word
PREFIX ="Prefix"   # Not an exact match, but a prefix (keep searching!)

# Special char for position in use
IN_USE = "@"

# Point values
POINTS = [0, 0, 0, 1, 1, 2, 3, 5, 11, 11, 11, 11, 11, 11, 11, 11, 11 ]

def read_dict(path: str) -> list[str]:
    """Returns ordered list of valid, normalized words from dictionary.

    >>> read_dict("data/shortdict.txt")
    ['ALPHA', 'BETA', 'DELTA', 'GAMMA', 'OMEGA']
    """
    result = []
    with open(path, newline="") as file:
        for row in file:
            word = row.strip()
            word = normalize(word)
            if allowed(word):
                result.append(word)
    result.sort()
    return result

def allowed(s: str) -> bool:
    """Is s a legal Boggle word?

    >>> allowed("am")  ## Too short
    False

    >>> allowed("de novo")  ## Non-alphabetic
    False

    >>> allowed("about-face")  ## Non-alphabetic
    False
    """
    if s.isalpha() and len(s) >= MIN_WORD:
        return True
    return False

def normalize(s: str) -> str:
    """Canonical for strings in dictionary or on board
    >>> normalize("filter")
    'FILTER'
    """
    return s.upper()

def search(candidate: str, word_list: list[str]) -> str:
    """Determine whether candidate is a MATCH, a PREFIX of a match, or a big NOPE
    Note word list MUST be in sorted order.

    >>> search("ALPHA", ['ALPHA', 'BETA', 'GAMMA']) == MATCH
    True

    >>> search("BE", ['ALPHA', 'BETA', 'GAMMA']) == PREFIX
    True

    >>> search("FOX", ['ALPHA', 'BETA', 'GAMMA']) == NOPE
    True

    >>> search("ZZZZ", ['ALPHA', 'BETA', 'GAMMA']) == NOPE
    True
    """
    low = 0
    high = len(word_list) - 1
    while high >= low:
        mid = (high + low) // 2
        if candidate == word_list[mid]:
            return MATCH
        elif candidate > word_list[mid]:
            low = mid + 1
        elif candidate < word_list[mid]:
            high = mid - 1
        # check whether substring
    if low < len(word_list) and word_list[low].startswith(candidate):
        return PREFIX
    else:
        return NOPE

def get_board_letters() -> str:
    """Get a valid string to form a Boggle board
    from the user.  May produce diagnostic
    output and quit.
    """
    while True:
        board_string = input(f"Input {BOARD_SIZE}-letter Boggle board (return to exit)> ")
        if allowed(board_string) and len(board_string) == BOARD_SIZE:
            return board_string
        elif len(board_string) == 0:
            print(f"OK, sorry it didn't work out")
            sys.exit(0)
        else:
            print(f'"{board_string}" is not a valid Boggle board')
            print(f'Please enter exactly 16 letters (or empty to quit)')

def unpack_board(letters: str) -> list[list[str]]:
    """Unpack a single string of characters into
    a matrix of individual characters, N_ROWS x N_COLS.

    >>> unpack_board("abcdefghijklmnop")
    [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p']]
    """
    result = []
    for i in range(N_ROWS):
        result.append([])
        for j in range(N_COLS):
            index = i * N_ROWS + j
            result[-1].append(letters[index])
    return result

def boggle_solve(board: list[list[str]], words: list[str]) -> list[str]:
    """Find all the words that can be made by traversing
    the boggle board in all 8 directions.  Returns sorted list without
    duplicates.

    >>> board = unpack_board("PLXXMEXXXAXXSXXX")
    >>> words = read_dict("data/dict.txt")
    >>> boggle_solve(board, words)
    ['AMP', 'AMPLE', 'AXE', 'AXLE', 'ELM', 'EXAM', 'LEA', 'MAX', 'PEA', 'PLEA', 'SAME', 'SAMPLE', 'SAX']
    """
    solutions = []

    def solve(row: int, col: int, prefix: str):
        """One solution step"""
        if row in range(N_ROWS) and col in range(N_COLS):
            # in the board
            letter = board[row][col]
            if letter != IN_USE:
                # not in use
                prefix = prefix + letter
                status = search(prefix, words)
                if status == NOPE:
                    pass
                if status == MATCH:
                    solutions.append(prefix)
                if status == MATCH or status == PREFIX:
                    # Keep searching
                    board[row][col] = IN_USE  # Prevent reusing
                    board_view.mark_occupied(row, col)
                    # Recursive calls to surrounding cells
                    for d_row in [0, -1, 1]:
                        for d_col in [0, -1, 1]:
                            solve(row + d_row, col + d_col, prefix)
                    # Restore letter for further search
                    board[row][col] = letter
                    board_view.mark_unoccupied(row, col)
                else:
                    pass
            else:
                pass
        else:
            pass

    # Look for solutions starting from each board position
    for row_i in range(N_ROWS):
        for col_i in range(N_COLS):
            solve(row_i, col_i, "")

    # Return solutions without duplicates, in sorted order
    solutions = list(set(solutions))
    return sorted(solutions)

def word_score(word: str) -> int:
    """Standard point value in Boggle"""
    assert len(word) <= 16
    return POINTS[len(word)]

def score(solutions: list[str]) -> int:
    """Sum of scores for each solution

    >>> score(["ALPHA", "BETA", "ABSENTMINDED"])
    14
    """
    points = 0
    for i in solutions:
        points += word_score(i)
    return points

def main():
    words = read_dict(config.DICT_PATH)
    board_string = get_board_letters()
    board_string = normalize(board_string)
    board = unpack_board(board_string)
    board_view.display(board)
    solutions = boggle_solve(board, words)
    board_view.prompt_to_close()
    print(solutions)
    print(f"{score(solutions)} points")

if __name__ == "__main__":
    doctest.testmod()
    print("Doctests complete")
    main()
