from src.solve import solve_from_file
import json


def assert_exercise(kind: str, exercise: int):
    answer = solve_from_file(
        f"tests/feature/data/{kind}/input/exercise{exercise}.json")

    with open(f"tests/feature/data/{kind}/output/answer{exercise}.json", "r") as answer_file:
        expected_answer = json.load(answer_file)
        assert answer == expected_answer
