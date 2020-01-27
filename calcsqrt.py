#! /usr/bin/env python3

# Conor Shortt
# Calculate the square root of a number using Python.

def sqrt(x):
    
    """
    Calculate the square root of argument x.
    """

    # Initial guess for the square root.
    z = x / 2.0

    # Continuousl improve guess
    while abs(x - (z*z)) > 0.01:
        z = z - (((z * z) - x) / (2 * z))
    
    return z

val = input("Please enter a number to get the square root of:\n")
val = float(val)
ans = sqrt(val)

print("The square root of ", val, " is ", ans)

