##
# 2WF90 Algebra for Security -- Software Assignment 1
# Integer and Modular Arithmetic
# solve.py
#
#
# Group number:
# 21
#
# Author names and student IDs:
# Thijs Notten (author_student_ID_1)
# Tom Nagel (author_student_ID_2)
# Vincent Hoogendam (author_student_ID_3)
# Christian Groothuis (1715534)
##

# Import built-in json library for handling input/output
import json
from src.basic_arithmetic import add, subtract
from src.multiplication import multiplication_karatsuba, multiplication_primary
from src.integer import Integer
from src.modular_arithmetic import mod_add, mod_subtract
from src.reduction import reduce


"""
1. addition/subtraction
2. multiplication
3. division
4. modular reduction
5. modular exponentiation"""


def solve(exercise: object):
    """
    solves an exercise specified in the file located at exercise_location and
    writes the answer to a file at answer_location. Note: the file at
    answer_location might not exist yet and, hence, might still need to be created.
    """
    radix = exercise["radix"]
    operation = exercise["operation"]
    x = Integer.from_string(exercise["x"], radix)

    # Check type of exercise
    if exercise["type"] == "integer_arithmetic":
        # Check what operation within the integer arithmetic operations we need to solve
        if operation == "addition":
            result = add(x, Integer.from_string(exercise["y"], radix)).to_string()

            return {"answer": result}

        elif operation == "subtraction":
            result = subtract(x, Integer.from_string(exercise["y"], radix)).to_string()

            return {"answer": result}

        elif operation == "multiplication_karatsuba" or operation == "multiplication":
            result = multiplication_karatsuba(x, Integer.from_string(exercise["y"], radix)).to_string()

            return {"answer": result}

        elif operation == "multiplication_primary":
            result = multiplication_primary(x, Integer.from_string(exercise["y"], radix)).to_string()

            return {"answer": result}
        
        # et cetera
    elif exercise["type"] == "modular_arithmetic":
        modulus = Integer.from_string(exercise["modulus"], radix)

        # Check what operation within the modular arithmetic operations we need to solve
        if operation == "reduction":
            result = reduce(x, modulus).to_string()

            return {"answer": result}
        if operation == "addition":
            result = mod_add(
                x, Integer.from_string(exercise["y"], radix), modulus
            ).to_string()

            return {"answer": result}

        if operation == "subtraction":
            result = mod_subtract(
                x, Integer.from_string(exercise["y"], radix), modulus
            ).to_string()

            return {"answer": result}
        # et cetera


def solve_from_file(exercise_location: str) -> object:
    with open(exercise_location, "r") as exercise_file:
        exercise = json.load(exercise_file)

    return solve(exercise)


def save_answer_to_file(answer_location: str, answer: object):
    with open(answer_location, "w") as answer_file:
        json.dump(answer, answer_file, indent=4)


def solve_exercise(exercise_location: str, answer_location: str):
    answer = solve_from_file(exercise_location)

    save_answer_to_file(answer_location, answer)
