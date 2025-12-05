from typing import List

## description of day ##
"""
You are given a list of product ID ranges and need to find the invalid IDs.

The ranges are separated by commas (,); each range gives its first ID and 
last ID separated by a dash (-).

you can find the invalid IDs by looking for any ID which is made only of some
sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice),
and 123123 (123 twice) would all be invalid IDs.

Pt 1:
Your job is to find all of the invalid IDs that appear in the given ranges
and add them up.

Pt 2:
Now, an ID is invalid if it is made only of some sequence of
digits repeated at least twice.
"""

## helper functions ##
def parse_input_file(file: str) -> List[tuple[int, int]]:
    """Read input file and create an array of id ranges,
        consisting of a start and stop ID.
        
        Returns the list of ID ranges"""
    
    # create array of ID ranges
    id_ranges = []

    with open(file, 'r') as input:
        for line in input:
            # split line into ranges
            ranges = line.split(',')

            # split ranges into start & stop ID
            for range in ranges:
                ids = range.split('-')

                # add range to list
                id_ranges.append(( int(ids[0]), int(ids[1]) ))

    return id_ranges

def find_invalid_ids(id_ranges: List[tuple[int, int]]) -> List[int]:
    """run through the list of ID ranges and pull out any invalid IDs.
        an invalid ID is one that is made only of some sequence of
        digits repeated twice.
        
        returns a list of invalid IDs"""

    invalid_ids = []

    # loop through each ID range
    for id_range in id_ranges:

        # loop through each ID in the range
        for gift_id in range(id_range[0], id_range[1]+1):
            
            # check if ID is invalid
            id_str = str(gift_id)
            midpoint = len(id_str) // 2  # Use integer division for the midpoint
            first_half = id_str[:midpoint]
            second_half = id_str[midpoint:]

            # check if the splits match
            if first_half == second_half:

                # add ID to list of invalid ones
                invalid_ids.append(gift_id)
                                   
    # return invalid IDs
    return invalid_ids

def find_invalid_ids2(id_ranges: List[tuple[int, int]]) -> List[int]:
    """run through the list of ID ranges and pull out any invalid IDs.
        an invalid ID is one that is made only of some sequence of
        digits repeated at least twice.
        
        returns a list of invalid IDs"""
    
    invalid_ids = []

    # loop through each ID range
    for id_range in id_ranges:

        # loop through each ID in the range
        for gift_id in range(id_range[0], id_range[1]+1):

            # convert to string
            id_str = str(gift_id)
            id_length = len(id_str)

            # loop through all possible sequences (stop when it gets to half the len)
            for seq_len in range(1, id_length//2 + 1):
                
                # check if original length can be perfectly divided by current sequence length
                if id_length % seq_len == 0:
                    
                    # create repeating sequence
                    seq = id_str[:seq_len]

                    # construct full sequence
                    repeat_seq = seq * (id_length // seq_len)

                    # check if sequence matches original ID
                    if id_str == repeat_seq:
                        # add invalid ID to list
                        invalid_ids.append(gift_id) 
                        # break to avoid repeats 
                        break

    return invalid_ids


## main ##
id_ranges = parse_input_file("day 2/input.txt")
invalid_ids = find_invalid_ids(id_ranges)

# get sum of invalid IDs
pt1_answer = 0
for gift_id in invalid_ids:
    pt1_answer += gift_id
print(f"pt1 answer: {pt1_answer}")

# complete part 2
invalid_ids = find_invalid_ids2(id_ranges)

# get sum of invalid IDs
pt2_answer = 0
for gift_id in invalid_ids:
    pt2_answer += gift_id
print(f"pt2 answer: {pt2_answer}")
