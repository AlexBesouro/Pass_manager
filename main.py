from  cryptography.fernet import Fernet

"""
Using only once to generate a key

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


write_key()
"""
def load_key():
    with open("key.key", "rb") as file:
        loaded_key = file.read()
    return loaded_key


key = load_key()
fer = Fernet(key)


def view_pass():
    acc_data = dict()
    with open("password_manager.txt", "r") as file:
        for line in file.readlines():
            line = line.strip().split("\t\t--|--\t\t")
            user, pwd = line
            acc_data[user] = fer.decrypt(pwd).decode()
    print(acc_data)

def add_pass():
    name = input("Account name:\n")
    pwd = input("Account password:\n")

    with open("password_manager.txt", "a") as file:
        file.write(f"{name}\t\t--|--\t\t{fer.encrypt(pwd.encode()).decode()}\n")


while True:

    user_choice = input("Would you like to add a new password or view existing ones (view / add), "
                        "enter q to quit:\n").lower()

    if user_choice.lower() == "q":
        break

    if user_choice == "view":
        view_pass()
    elif user_choice == "add":
        add_pass()
    else:
        print("Invalid choice")
        continue
