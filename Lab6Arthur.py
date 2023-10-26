def encoder():
    password = list(input('Please enter your password to encode: '))
    i = 0
    while i != len(password):
        password[i] = int(password[i])
        password[i] += 3
        password[i] = str(password[i])
        i += 1
    return ''.join(password)

def decoder(encoded_password):
    pass

def main():
    user_input = int(input('Please enter an option: '))
    while user_input != 3:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
        if user_input == 1:
            encoded_password = encoder()
            print('Your password has been encoded and stored!')
        elif user_input == 2:
            decoder(encoded_password)
        user_input = int(input('Please enter an option: '))

if __name__ == '__main__':
    main()
