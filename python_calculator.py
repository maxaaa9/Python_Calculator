from colorama import Back, Style, Fore


def addition(first_num, second_num):
    if first_num.is_integer() and second_num.is_integer():
        first_num = int(first_num)
        second_num = int(second_num)
    return f"{first_num} + {second_num} = {first_num + second_num}"


def subtraction(first_num, second_num) -> str:
    return f"{first_num} - {second_num} = {first_num - second_num}"


def multiplication(first_num, second_num) -> str:
    return f"{first_num} x {second_num} = {first_num * second_num:.2f}"


def division(first_num, second_num):
    if first_num == 0 or second_num == 0:
        return "You cant divide by 0!"
    return f"{first_num} / {second_num} = {first_num / second_num:.2f}"


def modulus(first_num, second_num):
    return f"{first_num} % {second_num} = {first_num % second_num:.2f}"


def main():
    while True:
        print(Style.BRIGHT + Back.WHITE + Fore.BLACK + "\nPython Calculator\nMenu:\n")
        print("    1.Addition (+)\n"
              "    2.Subtraction (-)\n"
              "    3.Multiplication (x)\n"
              "    4.Division (/)\n"
              "    5.Modulus (%)\n"
              "    6.Quit")
        selector = input(Style.NORMAL + "Enter your choice (1/2/3/4/5/6):")
        if selector.isdigit():
            selector = int(selector)
            if selector == 6:
                print("GoodBye!")
                break
            if 1 <= int(selector) < 7:
                first_number = float(input("Enter the first number:"))
                second_number = float(input("Enter the second number:"))
                print()
                result = 0
                if selector == 1:
                    result = addition(first_number, second_number)
                elif selector == 2:
                    result = subtraction(first_number, second_number)
                elif selector == 3:
                    result = multiplication(first_number, second_number)
                elif selector == 4:
                    result = division(first_number, second_number)
                elif selector == 5:
                    result = modulus(first_number, second_number)
                if result != 0:
                    print(Style.BRIGHT + f"    Result: {result}")


main()
