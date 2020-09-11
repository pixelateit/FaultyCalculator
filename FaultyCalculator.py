# 56+9=77, 56/6=4, 45*3=555
def calculator():
    inp_n1 = int(input("First number: "))
    inp_n2 = int(input("Second number: "))
    operators = ["+", "-", "/", "*", "**"]
    inp_op = input("Choose appropriate operator: \n"
                   "(+, -, /, *, **) \n  ")
    if inp_op not in operators:
        inp_op = input("Choose appropriate operator: \n"
                       "(+, -, /, *, **) \n  ")

    if inp_op == "+":
        if inp_n1 == 56 and inp_n2 == 9:
            print("77")
        else:
            print(f"{inp_n1+inp_n2}")
    elif inp_op == "-":
        print(f"{inp_n1-inp_n2}")
    elif inp_op == "*":
        if inp_n1 == 45 and inp_n2 == 3:
            print("555")
        else:
            print(f"{inp_n1*inp_n2}")
    elif inp_op == "/":
        if inp_n1 == 56 and inp_n2 == 6:
            print("4")
        else:
            print(f"{inp_n1/inp_n2}")
    elif inp_op == "**":
        print(f"{inp_n1**inp_n2}")
    again()


def again():
    cal_again = input("Press y if you want to continue or n if you want to end the calculator: ")

    if cal_again == "y":
        calculator()
    elif cal_again == "n":
        print("See ya!")
    else:
        again()


calculator()
