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


def solve(exercise: object):
    """
    solves an exercise specified in the file located at exercise_location and
    writes the answer to a file at answer_location. Note: the file at
    answer_location might not exist yet and, hence, might still need to be created.
    """
    x = exercise["x"]
    radix = exercise["radix"]
    operation = exercise["operation"]

    # Check type of exercise
    if exercise["type"] == "integer_arithmetic":
        # Check what operation within the integer arithmetic operations we need to solve
        if operation == "addition":
            # Solve integer arithmetic addition exercise
            pass
        elif operation == "subtraction":
            # Solve integer arithmetic subtraction exercise
            pass
        # et cetera
    elif exercise["type"] == "modular_arithmetic":
        # Check what operation within the modular arithmetic operations we need to solve
        if operation == "reduction":
            # Solve modular arithmetic reduction exercise
            pass
        # et cetera


    # Open file at answer_location for writing, creating the file if it does not exist yet
    # (and overwriting it if it does already exist).
    with open(answer_location, "w") as answer_file:
        # Serialize Python answer data (stored in answer) to JSON answer data and write it to answer_file
        json.dump(answer, answer_file, indent=4)


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
