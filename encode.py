def encoder(password):
    encoded_password = ""
    for i in password:
        encoded_password += str((int(i) + 3) % 10)
    return encoded_password
def decoder(password):
    decoded_password = ""
    for i in password:
        decoded_password += str((int(i) - 3) % 10)
    return decoded_password

def main():
    while True:
        print("Menu")
        print("-"*13)
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        user_input = input("Please enter an option: ")
        user_password = input("Please enter your password to encode: ")
        encoded_password = encoder(user_password)
        if user_input == '1':
            print("Your password has been encoded and stored!")
            print()
        elif user_password == '2':
            print(f"The encoded password is {encoded_password}, and the original password is {decoder(encoded_password)}")
            print()
        elif user_password == '3':
            False
if __name__ == "__main__":
    main()
