def main_code():
    name = ""
    names = []

    while name != "Stop":
        name = input("Please enter your name: ")
        names.append(name)
    
    names.pop()

    print("The people in the list are")
    
    for name in names:
        print(name)

    print()

    if len(names) >= 2:
        print("The second person in the list is " + names[1])
    
    if len(names) > 0:
        print("The last person in the list is " + names[-1])

if __name__ == "__main__":
    main_code()