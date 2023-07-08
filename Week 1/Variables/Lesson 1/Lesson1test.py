import io
from contextlib import redirect_stdout
from Lesson1code import main_code

def test_main():
    f = io.StringIO()
    with redirect_stdout(f):
        main_code()
    out = f.getvalue()
    assert out == "hello world\n"
    print("Congrats, you did it!")
if __name__ == "__main__":
    test_main()