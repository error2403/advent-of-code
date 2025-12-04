
stacks = [
    [],
    ['Z', 'N'],
    ['M', 'C', 'D'],
    ['P'],
]

with open('test.txt', 'r') as input:
    for line in input:
        if(line.startswith("move")):
            formatted = line.replace("move ", "")
            formatted = formatted.replace("\n", "")
            formatted = formatted.replace("to", "from")
            split = formatted.split(" from ")
            print(split)