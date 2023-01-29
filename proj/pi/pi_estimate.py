"""
pi_estimate.py

Estimate the value of Pi with Monte Carlo simulation.
(Just for kicks, also does Riemann sum method)

2022-10-04
by Alex Peterson Santos

Credit: Petraea (idea for Riemann sum method)
"""

import random
import doctest
import points_plot
import sys

GOOD_PI = 3.141592653589793
SAMPLES = 15000

def rand_point_unit_sq() -> tuple[float, float]:
    """Return random coord pair between (0..1, 0..1)"""
    return abs(random.random()), abs(random.random())

def in_unit_circle(x: float, y: float) -> bool:
    """Return True if coord pair in (0,0) circle radius 1
    
    >>> in_unit_circle(0.0, 0.0)
    True
    >>> in_unit_circle(1.0, 1.0)
    False
    >>> in_unit_circle(0.5, -0.5)
    True
    >>> in_unit_circle(-0.9, -0.5)
    False
    """
    if x**2 + y**2 < 1:
        return True
    else:
        return False

def plot_random_points(n_points: int = 500):
    """Solely for testing random distribution
    Generate and plot n_points points in interval (0..1, 0..1)
    Creates window and prompts user to close
    """
    points_plot.init()
    for i in range(n_points):
        x, y = rand_point_unit_sq()
        points_plot.plot(x, y, color_rgb=(50, 50, 50))
    points_plot.wait_to_close()

def relative_error(est: float, expected: float) -> float:
    """Return relative error of estimate as non-negative fraction of expected value.
    
    >>> round(relative_error(3.0, 5.0), 2)
    0.4
    >>> round(relative_error(5.0, 3.0), 2)
    0.67
    """
    abs_err = est - expected
    rel_err = abs(abs_err / expected)
    return rel_err

def pi_approx(samples: int = SAMPLES) -> float:
    """Return an estimate of pi by sampling random points.

    >>> relative_error(pi_approx(), GOOD_PI) <= 0.01  # Within 1%
    True
    >>> relative_error(pi_approx(), GOOD_PI) <= 0.01  # Within 1%
    True
    >>> relative_error(pi_approx(), GOOD_PI) <= 0.01  # Within 1%
    True
    """
    total = 0
    in_circle = 0   
    for i in range(samples):
        total += 1
        x, y = rand_point_unit_sq()
        if in_unit_circle(x, y):
            in_circle += 1
            points_plot.plot(x, y, color_rgb=(255, 10, 10)) ## Red
        else:
            points_plot.plot(x, y, color_rgb=(240, 240, 240)) ## Light grey
    est = in_circle / total * 4
    return est

def riemann_pi_approx(samples: int = SAMPLES) -> float:
    """Return an estimate of pi using a Riemann sum of vertical strips.

    >>> relative_error(riemann_pi_approx(), GOOD_PI) <= 0.01  # Within 1%
    True
    >>> relative_error(riemann_pi_approx(), GOOD_PI) <= 0.01  # Within 1%
    True
    >>> relative_error(riemann_pi_approx(), GOOD_PI) <= 0.01  # Within 1%
    True
    """
    circle_area = 0
    strip_width = 1 / samples
    for i in range(samples):
        x = (i*strip_width) + (strip_width/2)
        y = (1-x**2)**(1/2)
        strip_area = strip_width * y
        circle_area += strip_area
    est = circle_area * 4
    return est

def main():
    doctest.testmod()
    # plot_random_points() # eyeball test

    samples = SAMPLES  # allows overriding default constant
    method = "plot"
    
    for i in sys.argv:
        if i == "riemann":
            method = "riemann"
        elif i.isdigit():
            samples = int(i)
    
    if method == "riemann":
        print(f"Using Riemann sum method with {samples} vertical strips")
        est = riemann_pi_approx(samples)
    else:
        print(f"Using random points method with {samples} sample points")
        print("Pass 'riemann' in cmdline to use Riemann sum method (just for kicks)")
        points_plot.init()
        est = pi_approx(samples)

    rel_err = relative_error(est, GOOD_PI)
    print(f"\nPi is approximately {est}")
    print(f"Resulted in relative error of {rel_err}")

    if method == "plot":
        points_plot.wait_to_close()

    print("\nExiting...")
    exit()

if __name__ == "__main__":
    main()
