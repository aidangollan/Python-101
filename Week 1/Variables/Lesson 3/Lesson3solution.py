def main_code():
    score = input("Enter your score here ")
    score = int(score)
    if score < 60:
        print("The user's grade is a F")
    elif score < 70:
        print("The user's grade is a D")
    elif score < 80:
        print("The user's grade is a C")
    elif score < 90:
        print("The user's grade is a B")
    else:
        print("The user's grade is a A")

if __name__ == "__main__":
    main_code()