from typing import List
from collections import deque

## description of day ##
"""The safe has a dial with only an arrow on it; around the dial are the numbers 0
   through 99 in order. As you turn the dial, it makes a small click noise as it
   reaches each number.

   The attached document (your puzzle input) contains a sequence of rotations, one
   per line, which tell you how to open the safe. A rotation starts with an L or R
   which indicates whether the rotation should be to the left (toward lower numbers)
   or to the right (toward higher numbers). Then, the rotation has a distance value
   which indicates how many clicks the dial should be rotated in that direction.

   Pt 1:
   The password is the number of times the dial is left pointing at 0 after any
   rotation in the sequence.

   Pt 2:
   "Due to newer security protocols, please use password method 0x434C49434B until
   further notice."

   You remember from the training seminar that "method 0x434C49434B" means you're
   actually supposed to count the number of times any click causes the dial to
   point at 0, regardless of whether it happens during a rotation or at the end of one.
"""

## helper functions ##
def parse_input_file(file: str) -> List[tuple[str, int]]:
    """Read input file and create an array of dial rotations,
        consisting of a direction(L,R) and a distance.
        
        Returns the list of rotations."""

    # full list of rotations
    rotations = []

    # components of rotations
    direction = ''
    distance = -1

    # parse the file line by line
    with open(file, 'r') as input:
        for line in input:
            # grab components from line
            direction = line[0]
            distance = int(line[1:])
            

            # add rotation to list
            rotations.append((direction, distance))

    # return parsed data
    return rotations


def rotate_dial(rotations: List[tuple[str, int]]) -> int:
    """Take a list of rotations and spin a dial per the instructions of
        each rotation (direction and distance).
        
        Returns the number of times the dial stopped at 0."""

    password = 0

    # set up dial
    dial_array = []
    for i in range(0, 100):
        dial_array.append(i)
    dial = deque(dial_array)

    # rotate dial to 50 (starting pos)
    dial.rotate(50)

    # rotate through list
    for rotation in rotations:
        direction = rotation[0]
        distance = rotation[1]

        # invert distance if direction is Left
        if direction == 'L':
            distance = -distance

        # rotate dial
        dial.rotate(distance)

        # check if dial is pointing at zero
        if dial[0] == 0:
            password += 1

    # return password
    return password


def rotate_dial_pt2(rotations: List[tuple[str, int]]) -> int:
    """Take a list of rotations and spin a dial per the instructions of
        each rotation (direction and distance).
        
        Returns the number of times the dial passed 0."""

    password = 0

    # set up dial
    dial_array = []
    for i in range(0, 100):
        dial_array.append(i)
    dial = deque(dial_array)

    # rotate dial to 50 (starting pos)
    dial.rotate(50)

    # rotate through list
    for rotation in rotations:
        direction = rotation[0]
        distance = rotation[1]

        # rotate dial
        for _ in range(distance):
            # invert distance if direction is Left
            if direction == 'L':
                dial.rotate(-1)
            else:
                dial.rotate(1)

            # check if it points at zero
            if dial[0] == 0:
                password += 1

    # return password
    return password

## main ##
rotations = parse_input_file("day 1/input_pt1.txt")
password_pt1 = rotate_dial(rotations)
password_pt2 = rotate_dial_pt2(rotations)

print(password_pt1)
print(password_pt2)