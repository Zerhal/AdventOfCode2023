import re

def read_file(file_name):
    """
    Read the file and return its content as a string.
    """
    with open(file_name, 'r') as file:
        return file.read()

def gear_ratios_part_one(file_content):
    # Lists to store coordinates of numeric values and symbols
    numeric_coordinates = []
    symbol_coordinates = []
    
    # Iterate through each line in the file_content
    for x, line in enumerate(file_content.split('\n')):
        # Find numeric values and their coordinates
        numeric_values = re.finditer(r'\d+', line)
        for numeric_value in numeric_values:
            coordinates = [(x, numeric_value.start() + i) for i in range(len(numeric_value.group()))]
            numeric_coordinates.append([numeric_value.group(), coordinates])
        
        # Find symbols (non-numeric characters) and their coordinates
        symbols = re.finditer(r'[^.\d]', line)
        for symbol in symbols:
            symbol_coordinates.append([symbol.group(), (x, symbol.start())])
    
    # List to store adjacent numeric values
    adjacent_numerics = []
    for numeric_value in numeric_coordinates:
        for coordinate in numeric_value[1]:
            for symbol in symbol_coordinates:
                # Check if the numeric value is adjacent to a symbol
                if abs(coordinate[0] - symbol[1][0]) <= 1 and abs(coordinate[1] - symbol[1][1]) <= 1:
                    adjacent_numerics.append(numeric_value) if numeric_value not in adjacent_numerics else None
                    break

    print('Part 1:', sum([int(numeric_value[0]) for numeric_value in adjacent_numerics]))       

def gear_ratios_part_two(file_content):
    # Lists to store coordinates of numeric values and symbols
    numeric_coordinates = []
    symbol_coordinates = []
    
    # Iterate through each line in the file_content
    for x, line in enumerate(file_content.split('\n')):
        # Find numeric values and their coordinates
        numeric_values = re.finditer(r'\d+', line)
        for numeric_value in numeric_values:
            coordinates = [(x, numeric_value.start() + i) for i in range(len(numeric_value.group()))]
            numeric_coordinates.append([int(numeric_value.group()), coordinates])
        
        # Find symbols (asterisks) and their coordinates
        symbols = re.finditer(r'[*]', line)
        for symbol in symbols:
            symbol_coordinates.append([symbol.group(), (x, symbol.start()), []])
    
    # Assign numeric values to symbols based on adjacency
    for numeric_value in numeric_coordinates:
        for coordinate in numeric_value[1]:
            for symbol in symbol_coordinates:
                # Check if the numeric value is adjacent to a symbol
                if abs(coordinate[0] - symbol[1][0]) <= 1 and abs(coordinate[1] - symbol[1][1]) <= 1:
                    symbol[2].append(numeric_value) if numeric_value not in symbol[2] else None
                    break

    # Print the result for Part 2
    print('Part 2:', sum([symbol[2][0][0] * symbol[2][1][0] for symbol in symbol_coordinates if len(symbol[2]) == 2]))

# Specify the input file name
file_name = 'input.txt'
# Read the content of the file
file_content = read_file(file_name)

# Execute both functions with the input content
gear_ratios_part_one(file_content)
gear_ratios_part_two(file_content)
