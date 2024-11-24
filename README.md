README.md

Lagrange Interpolation in Python

This project implements the Lagrange interpolation method in Python using the sympy library. The code calculates a polynomial that passes through a given set of points and verifies its accuracy by evaluating the polynomial at the input points.

Features

	•	Constructs a Lagrange interpolation polynomial from given ￼ and ￼ values.
	•	Simplifies the resulting polynomial for better readability.
	•	Verifies the correctness of the interpolation by evaluating the polynomial at the input points.

Requirements

Ensure you have Python installed along with the required library:
	•	Python 3.6 or higher
	•	sympy

To install sympy, use:

pip install sympy

Usage

	1.	Clone the repository or copy the script to your local machine.
	2.	Run the script:

python lagrange_interpolation.py


	3.	Input the ￼ and ￼ values as comma-separated lists when prompted. For example:

Input all the x values separated by comas: 1, 2, 3, 4
Input all the y values separated by comas: 3, 6, 19, 44

Example

Input:

For the points:
￼

Output:

The script calculates the Lagrange interpolation polynomial:
￼

Verification:

P(1) = 3, Expected value = 3
P(2) = 6, Expected value = 6
P(3) = 19, Expected value = 19
P(4) = 44, Expected value = 44

Code Structure

Functions

LaGrange(valoresX, valoresY)

Purpose: Performs the Lagrange interpolation and verifies its accuracy.
Parameters:
	•	valoresX: List of ￼-coordinates.
	•	valoresY: List of ￼-coordinates.
Returns: Simplified Lagrange polynomial.

__main__()

Purpose: Handles user input for the ￼ and ￼ values and calls the LaGrange function.

Error Handling

	•	If the lengths of the ￼ and ￼ arrays do not match, the program will display an error message:

Arrays don't have the same length.


	•	If the polynomial fails to evaluate correctly at any point, the program raises an assertion error.

License

This code is provided under the MIT License. Feel free to modify and distribute it as needed.

Authors

Juan Sebastian Morales Rincon
Alejandro Fontalvo Gomez
Sibeli Isaeth Rodriguez Diaz
Alejandro Rovira Brieva
Yhosimar Rafael Orozco Mosquera
Marlon Piñeres Melo


For questions or suggestions, feel free to reach out!
