# Amanda
print('This is mine')
print("HI")
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

