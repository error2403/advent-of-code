from typing import List

## description of day ##
"""
Batteries are each labeled with their joltage rating, 
a value from 1 to 9. You make a note of their joltage ratings 
(your puzzle input).

batteries are arranged into banks; each line of digits in your 
input corresponds to a single bank of batteries. Within each 
bank, you need to turn on exactly two batteries; the joltage 
that the bank produces is equal to the number formed by 
the digits on the batteries you've turned on.

You'll need to find the largest possible joltage each bank can produce.

Pt 1:
Turn on 2 batteries in each bank to create the largets possible joltage.
The total output joltage is the sum of the maximum joltage from each bank.

Pt 2:
Now, you need to make the largest joltage by turning on exactly twelve
batteries within each bank.
"""

## helper functions ##
def parse_input_file(file: str) -> List[List[int]]:
    """Read input file and create create an array of banks.
        Each bank is an array of batteries it contains.
        
        Returns the array of battery banks"""
    
    bank_array = []

    with open(file, 'r') as input:
        for line in input:

            bank = []
            # grab each battery in the bank(line)
            for char in line.rstrip():
                bank.append(int(char))

            # add bank to array of banks
            bank_array.append(bank)

    return bank_array

def get_bank_joltages(battery_banks: List[List[int]]) -> List[int]:
    """Find the highest joltage in each bank (highest 2 batteries).
    
        returns a list of the voltages."""
    
    joltages = []

    # loop through all banks
    for bank in battery_banks:
        
        # find highest battery (pos, battery jolt)
        highest = (-1, -1)
        for i in range(len(bank)-1):
            if bank[i] > highest[1]:
                highest = (i, bank[i])

        # find second highest (pos, battery jolt)
        second = (-1, -1)
        for i in range(highest[0]+1, len(bank)):
            if bank[i] > second[1]:
                second = (i, bank[i])

        # combine into joltage
        jolt = highest[1]*10 + second[1]
        joltages.append(jolt)

    return joltages


def get_bank_joltages_pt2(battery_banks: List[List[int]]) -> List[int]:
    """Find the highest joltage in each bank (highest 12 batteries).
    
        returns a list of the voltages."""
    
    joltages = []

    # loop through all banks
    for bank in battery_banks:

        # loop for 12 batteries
        batteries = [(-1, -1)]
        for i in range(12):

            # find highest battery (pos, battery jolt)
            highest = (-1, -1)
            for j in range(batteries[i][0]+1, len(bank)-(12-len(batteries))):
                if bank[j] > highest[1]:
                    highest = (j, bank[j])

            batteries.append(highest) 

        # remove filler first battery
        batteries.pop(0)

        # compute joltage for bank
        jolt = 0
        for i in range(12):
            jolt += batteries[i][1] * 10**(11-i)

        joltages.append(jolt)  

    return joltages


## main ##
battery_banks = parse_input_file("day 3/input.txt")
joltages = get_bank_joltages(battery_banks)

# add joltages
max_joltage = 0
for jolt in joltages:
    max_joltage += jolt
print(max_joltage)

# pt 2
joltages = get_bank_joltages_pt2(battery_banks)

# add joltages
max_joltage = 0
for jolt in joltages:
    max_joltage += jolt
print(max_joltage)