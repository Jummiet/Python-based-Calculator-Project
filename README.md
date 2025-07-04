# Console Calculator in Python

This is a simple console-based calculator application implemented in Python. The calculator supports three basic arithmetic operations: **Addition**, **Subtraction**, and **Division**. 
It also includes unit tests written using Python's built-in `unittest` framework.

---

## Project Structure


#calculator/
- calculator.py # Main calculator functions and console interface
- test_calculator.py # Unit tests for calculator functions
- README.md # Project documentation

---

## Features

- Addition of two numbers
- Subtraction of two numbers
- Division with error handling for division by zero
- Unit tests covering typical and edge cases

---

## Requirements

- Python 3.x

- No external libraries are needed.

---
 
 ## Test Coverage
This project includes comprehensive unit tests using Python’s built-in unittest framework. The test suite is designed to validate the functionality and robustness of the calculator operations.

Each function — add(), subtract(), and divide() — is tested with typical and edge case inputs to ensure correctness, error handling, and expected behavior.

## Test Scenarios:
1. Addition Tests

- Addition of two positive numbers (e.g., add(10, 5))
- Addition of two negative numbers (edge case)
- Addition with mixed signs (positive and negative)

2. Subtraction Tests
- Subtraction of two positive numbers
- Subtraction resulting in a negative number (edge case)
- Subtraction of two negative numbers

3. Division Tests
- Division of two positive numbers
- Division with a negative result
- Division resulting in a float
- Division of zero by a number (edge case)
- Division by zero — this is intentionally tested to confirm that a ValueError is raised correctly

# Assertions Used
The tests rely on assertions such as:
- assertEqual() for checking expected return values
- assertRaises() to verify that exceptions like division by zero are properly handled

## How to Run Tests

1. Ensure you have Python 3 installed.
2. Clone or download the project directory.
3. Open a terminal and navigate to the project directory.
4. Run the tests:
   python test_calculator.py
5. You should see output similar to:

   ...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK

## Usage Instructions
To run the calculator from the console:
   python calculator.py

## Author
Developed as part of a structured coding and testing practice project.


## License
This project is open-source and available for educational and personal use.


```bash
python calculator.py

python test_calculator.py

