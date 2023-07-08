from unittest.mock import patch
from Lesson3code import main_code
import io
from contextlib import redirect_stdout

def test_main():
    # Test 1: grade is 'F'
    with patch('builtins.input', return_value='50'):
        f = io.StringIO()
        with redirect_stdout(f):
            main_code()
        out = f.getvalue()
        assert out == "The user's grade is a F\n", "Test 1 failed: output was {}".format(out)

    # Test 2: grade is 'D'
    with patch('builtins.input', return_value='65'):
        f = io.StringIO()
        with redirect_stdout(f):
            main_code()
        out = f.getvalue()
        assert out == "The user's grade is a D\n", "Test 2 failed: output was {}".format(out)
    
    # Test 2: grade is 'C'
    with patch('builtins.input', return_value='75'):
        f = io.StringIO()
        with redirect_stdout(f):
            main_code()
        out = f.getvalue()
        assert out == "The user's grade is a C\n", "Test 2 failed: output was {}".format(out)

    # Test 2: grade is 'B'
    with patch('builtins.input', return_value='85'):
        f = io.StringIO()
        with redirect_stdout(f):
            main_code()
        out = f.getvalue()
        assert out == "The user's grade is a B\n", "Test 2 failed: output was {}".format(out)
    
    # Test 2: grade is 'A'
    with patch('builtins.input', return_value='95'):
        f = io.StringIO()
        with redirect_stdout(f):
            main_code()
        out = f.getvalue()
        assert out == "The user's grade is a A\n", "Test 2 failed: output was {}".format(out)
    
    # Test 2: grade is 'B' edge case
    with patch('builtins.input', return_value='80'):
        f = io.StringIO()
        with redirect_stdout(f):
            main_code()
        out = f.getvalue()
        assert out == "The user's grade is a B\n", "Test 2 failed: output was {}".format(out)
    
    # Test 2: grade is '70'
    with patch('builtins.input', return_value='70'):
        f = io.StringIO()
        with redirect_stdout(f):
            main_code()
        out = f.getvalue()
        assert out == "The user's grade is a C\n", "Test 2 failed: output was {}".format(out)

    print("Congrats, you did it!")

if __name__ == "__main__":
    test_main()