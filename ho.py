# Amanda
# making encoder

def encoder(password):
    password = str(password)
    new_pass_list = []
    for num in password:
        num = int(num)
        num += 3
        new_pass_list.append(str(num))
    new_pass = "".join(new_pass_list)
    return new_pass


def menu_display():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


while True:
    menu_display()
    user_input = input("Please enter an option: ")
    if user_input == "1" or user_input == "2":
        password = input("Please enter your password to encode: ")
        print("Your password has been encoded and stored!")
        menu_display()
        if
    else:
        break
