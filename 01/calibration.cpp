#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

int main()
{
    // Open the file input.txt
    std::ifstream inputFile("input.txt");

    if (!inputFile.is_open())
    {
        std::cerr << "Error: input.txt" << std::endl;
        return 1;
    }

    // Initialize the sum of calibration values
    int sumOfCalibrationValues = 0;

    // Iterate through each line of the file
    std::string line;
    while (std::getline(inputFile, line))
    {
        // Initialize two variables to store the first and last digit of each line
        char firstDigit = 0, lastDigit = 0;

        // Iterate through each character of the line
        for (char ch : line)
        {
            // If the character is a digit, update firstDigit
            if (std::isdigit(ch))
            {
                if (!firstDigit)
                {
                    firstDigit = ch;
                }
                lastDigit = ch;
            }
        }

        // Combine the two digits to form a two-digit number
        int calibrationValue = (firstDigit - '0') * 10 + (lastDigit - '0');

        // Add the calibration value to the total sum
        sumOfCalibrationValues += calibrationValue;
    }

    // Close the file
    inputFile.close();

    // Display the total sum of calibration values
    std::cout << "Sum: " << sumOfCalibrationValues << std::endl;

    return 0;
}
