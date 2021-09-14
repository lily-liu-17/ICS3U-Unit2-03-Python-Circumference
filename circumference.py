#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Sept 2021
# This program calculates the circumference using tau
#    with radius inputted from the user

import consatant


def main():
    # This program calculates the circumference using tau

    # input
    radius = int(input("Enter the radius of the circle (cm) : "))

    # process
    circumference = consatant.TAU * radius

    # output
    print("")
    print("The circumference is {0} cm.".format(circumference))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
