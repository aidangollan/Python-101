from unittest.mock import patch
from Lesson2code import main_code
import io
from contextlib import redirect_stdout

def test_main():
    # Test 1: name is 'Dan'
    with patch('builtins.input', return_value='Dan'):
        f = io.StringIO()
        with redirect_stdout(f):
            main_code()
        out = f.getvalue()
        assert out == "The user's name is Dan\n", "Test 1 failed: output was {}".format(out)

    # Test 2: name is 'Bob'
    with patch('builtins.input', return_value='Bob'):
        f = io.StringIO()
        with redirect_stdout(f):
            main_code()
        out = f.getvalue()
        assert out == "The user's name is Bob\n", "Test 2 failed: output was {}".format(out)

    print("Congrats, you did it!")

if __name__ == "__main__":
    test_main()