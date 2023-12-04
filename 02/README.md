Advent of Code 2023 - Day 2: Cube Conundrum
===========================================

Problem Description
-------------------

In this festive adventure, you find yourself on Snow Island, where an Elf challenges you to play a game involving cubes of different colors. The Elf loads a bag with cubes and reveals subsets of them during each game. Your task is to analyze the games and answer two questions.

### Part One

The Elf asks which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes. The games are identified by unique ID numbers, and you need to calculate the sum of the IDs for the possible games.

### Part Two

Now, the Elf is concerned about the lack of water and poses a second question. For each game, determine the minimum number of cubes of each color needed to make the game possible. The power of a set of cubes is the product of the numbers of red, green, and blue cubes. Find the sum of these powers for all games.

Implementation
--------------

The solution is implemented in Python, and the code is organized into two functions:

-   `cube_conundrum_part_one(file_content)`: Solves Part One of the problem.
-   `cube_conundrum_part_two(file_content)`: Solves Part Two of the problem.

Additionally, there is a helper function:

-   `read_file(file_name)`: Reads the content of the input file and returns it as a string.

Input
-----

The input file ('input.txt') contains records of games played on Snow Island. Each game is listed with its ID number and a semicolon-separated list of subsets of cubes that were revealed during the game.

Output
------

The output is printed for both parts of the problem. For Part One, it displays the sum of the IDs of the possible games. For Part Two, it shows the sum of the powers of the minimum sets of cubes required for each game.

Usage
-----

To run the code, execute the 'main.py' script:


`python main.py`

The script will read the input file, solve both parts of the problem, and print the results.