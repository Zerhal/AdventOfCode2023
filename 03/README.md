Advent of Code 2023 - Day 3: Gear Ratios
========================================

Problem Description

You find yourself at a gondola lift station with an unexpected problem - the gondola lift isn't working. An Elf engineer needs your help to identify a missing part from the engine using an engine schematic. Your task is to sum up part numbers adjacent to symbols and, in Part Two, calculate gear ratios for specific symbols.

### Part One

The engine schematic is a visual representation of the engine, including numbers and symbols. You need to sum all the numbers adjacent to symbols, even diagonally. Symbols are identified as non-numeric characters, excluding periods (.) from consideration.

*Example:*

plaintextCopy code

`467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..`

In this example, the sum of part numbers is 4361. Your task is to calculate the sum of all part numbers in the actual, larger engine schematic.

### Part Two

After identifying the missing part, you encounter another issue - incorrect gears in the engine. Gears are * symbols adjacent to exactly two part numbers. The gear ratio is the result of multiplying these two numbers together.

*Example:*

plaintextCopy code

`467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..`

In this example, there are two gears with ratios 16345 and 451490. The task is to find the gear ratio for every gear and sum them up.


Implementation

The solution is implemented in Python, and the code is organized into two functions:

-   `gear_ratios_part_one(file_content)`: Identifies numeric values adjacent to symbols and sums them up.
-   `gear_ratios_part_two(file_content)`: Calculates gear ratios for symbols and sums them up.

Additionally, there is a helper function:

-   `read_file(file_name)`: Reads the content of the input file and returns it as a string.

Input

The input file ('input.txt') contains an engine schematic with numeric values and symbols.

Output

The output is printed for both parts of the problem. For Part One, it displays the sum of the IDs of the possible games. For Part Two, it shows the sum of the powers of the minimum sets of cubes required for each game.

Usage

To run the code, execute the 'main.py' script:

`python main.py`

The script will read the input file, solve both parts of the problem, and print the results.