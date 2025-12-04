from typing import List
from collections import deque

## description of day ##
## TODO


## helper functions ##
def parse_input_file(file: str) -> List[tuple[str, int]]:
    """TODO: description"""

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
    """TODO: description"""

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
    """TODO: description"""

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