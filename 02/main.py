import re

def read_file(file_name):
    """
    Open the file in read ('r') mode and return its content as a string.
    """
    with open(file_name, 'r') as file:
        return file.read()

def cube_conundrum_part_one(file_content):
    """
    Solve Part 1 of the cube conundrum problem.

    Parameters:
    - file_content (str): The content of the input file as a string.
    """
    # Find all matches for the game pattern in the file content
    games = re.findall(r'(\d+):((?: *\d+\s+\w+,?;?)+)', file_content)
    
    # Initialize total count
    total_count = sum([int(game[0]) for game in games])

    # Iterate through each game
    for game in games:
        # Find all matches for the die pattern in the current game
        dice = re.findall(r'(\d+)\s+(\w+)', game[1])
        
        # Iterate through each die in the game
        for die in dice:
            n, c = int(die[0]), die[1]
            
            # Check conditions and subtract from total count if needed
            if (n > 12 and c == 'red') or (n > 13 and c == 'green') or (n > 14 and c == 'blue'):
                total_count -= int(game[0])
                break

    # Print the result for Part 1
    print('Part 1:', total_count)

def cube_conundrum_part_two(file_content):
    """
    Solve Part 2 of the cube conundrum problem.

    Parameters:
    - file_content (str): The content of the input file as a string.
    """
    # Find all matches for the game pattern in the file content
    games = re.findall(r'(\d+):((?: *\d+\s+\w+,?;?)+)', file_content)
    
    # Initialize total power
    total_power = 0

    # Iterate through each game
    for game in games:
        # Find all matches for the die pattern in the current game
        dice = re.findall(r'(\d+)\s+(\w+)', game[1])
        
        # Initialize a dictionary to store values for each color
        type_dict = {'red': [], 'green': [], 'blue': []}

        # Iterate through each die in the game
        for die in dice:
            n, c = int(die[0]), die[1]
            
            # Append the value to the corresponding color's list
            type_dict[c].append(int(n))

        # Calculate the total power for the current game and add to the overall total power
        total_power += max(type_dict['red']) * max(type_dict['green']) * max(type_dict['blue'])

    # Print the result for Part 2
    print('Part 2:', total_power)

# Specify the input file name
file_name = 'input.txt'
# Read the content of the file
file_content = read_file(file_name)
# Execute the functions for both parts
cube_conundrum_part_one(file_content)
cube_conundrum_part_two(file_content)
