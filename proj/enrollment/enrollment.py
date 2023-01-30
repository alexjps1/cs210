"""
enrollment.py
Enrollment analysis: Summary report of majors enrolled in a class.
CS 210 project, Fall 2022.

2022-10-17
Author:  Alex JPS
Credits: N/A
"""

import doctest
import csv

ROSTER="./data/roster_selected.csv"
PROGRAMS="./data/programs.csv"

# ROSTER="./data/test_roster.csv"
# PROGRAMS="./data/test_programs.csv"

def read_csv_column(path: str, field: str) -> list[str]:
    """Read one column from a CSV file with headers into a list of strings.

    >>> read_csv_column("./data/test_roster.csv", "Major")
    ['DSCI', 'CIS', 'BADM', 'BIC', 'CIS', 'GSS']
    """
    result = []
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            result.append(row[field])
    return result

def counts(column: list[str]) -> dict[str, int]:
    """Returns a dict with counts of elements in column.

    >>> counts(["dog", "cat", "cat", "rabbit", "dog"])
    {'dog': 2, 'cat': 2, 'rabbit': 1}
    """
    counts = {}
    for i in column:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts

def read_csv_dict(path: str, key_field: str, value_field: str) -> dict[str, dict]:
    """Read a CSV with column headers into a dict with selected
    key and value fields.

    >>> read_csv_dict("./data/test_programs.csv", key_field="Code", value_field="Program Name")
    {'ABAO': 'Applied Behavior Analysis', 'ACTG': 'Accounting', 'ADBR': 'Advertising and Brand Responsibility'}
    """
    result = {}
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            result[row[key_field]] = row[value_field]
    return result

def items_v_k(to_pair: dict) -> list[tuple]:
    """Convert given dict to list of tuples of form (value, key)

    >>> items_v_k({"cats": 1, "dogs": 3, "rats": 2})
    [(1, 'cats'), (3, 'dogs'), (2, 'rats')]
    """
    result = []
    for key, value in to_pair.items():
        pair = (value, key)
        result.append(pair)
    return result
    
def main():
    doctest.testmod()

    majors_list = read_csv_column(ROSTER, "Major")
    majors_counts = counts(majors_list)
    program_names = read_csv_dict(PROGRAMS, "Code", "Program Name")

    by_count = items_v_k(majors_counts)
    by_count.sort(reverse=True)

    for count, code in by_count:
        program = program_names[code]
        print(count, program)

if __name__ == "__main__":
    main()
