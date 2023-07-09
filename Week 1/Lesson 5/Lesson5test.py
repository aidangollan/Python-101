from unittest.mock import patch
from Lesson5code import main_code
import io
from contextlib import redirect_stdout

def test_main():
    # Test 1
    grades = {"Sam" : ["A", "A", "B", "C", "F"], "Bill": ["C", "B", "C", "A", "C"], "John" : ["A", "A", "B", "A", "B"]}
    f = io.StringIO()
    with redirect_stdout(f):
        ret = main_code(grades)
    out = f.getvalue()

    # Prepare expected output
    expected_output = "The letter grade for Sam is C\nThe letter grade for Bill is B\nThe letter grade for John is A\nThe best student is John with a grade of A\nThe worst student is Sam with a grade of C\nThe scores that showed up are\nA\nB\nC"
    
    assert out == expected_output, "Test 1 failed: output was {}".format(out)

    assert ret == 100


    print("Congrats, you did it!")

if __name__ == "__main__":
    test_main()