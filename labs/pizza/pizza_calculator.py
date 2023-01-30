"""
pizza_calculator.py
Calculates cost per square inch of a pizza based on diameter and total cost.

2022-10-12
by Alex JPS
"""

import math 
import doctest

def circle_area(diameter) -> float:
    """
    (float or int) -> float

    Return area of circle given its diameter

    >>> round(circle_area(2), 4)
    3.1416

    >>> round(circle_area(10), 4)
    78.5398
    """ 
    radius = diameter / 2
    area = math.pi * radius**2
    return area

def pizza_calculator(diameter: int, cost) -> float:
    """ 
    (int, float) -> float 

    Calculates and returns the cost per square inch 
    of pizza for a pizza of given diameter and cost. 
    Examples: 

    >>> pizza_calculator(14, 18) 
    0.117
    >>> pizza_calculator(14, 20.25)  
    0.132
    """ 
    area = circle_area(diameter)

    cost_per_inch = cost / area 
    cost_per_inch = round(cost_per_inch, 3) 
    return cost_per_inch

def main():
    print(doctest.testmod())

if __name__ == "__main__":
    main()
