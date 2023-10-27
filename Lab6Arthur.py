def encoder():
    password = list(input('Please enter your password to encode: '))
    i = 0
    while i != len(password):
        password[i] = int(password[i])
        password[i] += 3
        if password[i] == 10:
            password[i] = 0
        elif password[i] == 11:
            password[i] = 1
        elif password[i] == 12:
            password[i] = 2
        password[i] = str(password[i])
        i += 1
    return ''.join(password)

def decoder(encoded_password):
    password = str(encoded_password)
    decoded = ""
    for i in range(0, 8):
        value = int(password[i]) - 3
        if value < 0:
            value = 10 + value
        decoded = decoded + str(value)
    return decoded

def main():
    user_input = int(input('Please enter an option: '))
    while user_input != 3:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
        if user_input == 1:
            encoded_password = encoder()
            print('Your password has been encoded and stored!')
        elif user_input == 2:
            print("The encoded password is " + encoded_password + ", and the original password is " + decoder(encoded_password) +".")
        user_input = int(input('Please enter an option: '))

if __name__ == '__main__':
    main()
