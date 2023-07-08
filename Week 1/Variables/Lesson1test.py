import io
from contextlib import redirect_stdout
from Lesson1code import main_code

def test_main():
    f = io.StringIO()  # Create StringIO object
    with redirect_stdout(f):  # Redirect stdout to StringIO object
        main_code()  # Call function
    out = f.getvalue()  # Get stdout
    assert out == "hello world\n"  # Compare stdout with the expected output
    print("Congrats, you did it!")
if __name__ == "__main__":
    test_main()