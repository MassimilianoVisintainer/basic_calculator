# Simple Calculator in Python

This Python script provides a simple command-line calculator with basic arithmetic operations: addition, subtraction, multiplication, and division.

## Usage

1. **Function Descriptions:**

   - `add(a, b)`: Performs addition of two numbers (`a` and `b`).
   - `sub(a, b)`: Performs subtraction of two numbers (`a` and `b`).
   - `mul(a, b)`: Performs multiplication of two numbers (`a` and `b`).
   - `div(a, b)`: Performs division of two numbers (`a` and `b`).

   Each function takes two inputs (`a` and `b`), performs the specified operation, and displays the result.

2. **How to Use:**

   - Run the Python script.
   - The program will display a menu with options for addition, subtraction, multiplication, division, and quitting the program.
   - Select an option by entering the corresponding letter (e.g., 'A' for addition, 'B' for subtraction, etc.).
   - Input the two numbers when prompted.
   - The program will display the result of the selected operation.

3. **Example:**

   ```python
   def add(a, b):
       answer = int(a) + int(b)
       print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

   # Other functions (sub, mul, div) have similar structures...

   while True:
       # Display options and perform operations based on user input...
       # (Your existing while loop logic goes here)
