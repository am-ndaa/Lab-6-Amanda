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

def decoder(password):
    list_num = []
    enc_list = []
    num_str = ''
    password= str(password)
    for num in password:
        list_num.append(num)
    for num in list_num:
        num = int(num)
        num -= 3
        enc_list.append(num)
    for num in enc_list:
        num = str(num)
        num_str += num
    return num_str



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
