from unittest.mock import patch
from Lesson4code import main_code
import io
from contextlib import redirect_stdout

def test_main():
    # Test 1: names are "John", "James", "Bob", "Stop"
    with patch('builtins.input', side_effect=['John', 'James', 'Bob', 'Stop']):
        f = io.StringIO()
        with redirect_stdout(f):
            main_code()
        out = f.getvalue()

        # Prepare expected output
        expected_output = "The people in the list are\nJohn\nJames\nBob\n\nThe second person in the list is James\nThe last person in the list is Bob\n"
        
        assert out == expected_output, "Test 1 failed: output was {}".format(out)

    # Test 1: names are "Stop"
    with patch('builtins.input', side_effect=['Stop']):
        f = io.StringIO()
        with redirect_stdout(f):
            main_code()
        out = f.getvalue()

        # Prepare expected output
        expected_output = "The people in the list are\n\n"
        
        assert out == expected_output, "Test 2 failed: output was {}".format(out)

    print("Congrats, you did it!")

if __name__ == "__main__":
    test_main()