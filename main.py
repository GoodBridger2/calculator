def calculate():
    a = int(input("First Number:"))
    b = int(input("Second Number:"))
    operator = input("Choose +, -, *, /:")
    if operator == ("+"):
        print(a+b)
    elif operator == ("-"):
        print(a-b)
    elif operator == ("*"):
        print(a*b)
    else:
        print(a/b)
    request = input("Again? y/n :")
    if request == ("y"):
        calculate()
    else:
        exit()