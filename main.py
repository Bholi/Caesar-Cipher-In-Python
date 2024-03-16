from art import logo

print(logo)


def caesar(message, shifts, cipher_direction):
    cipher_text = ''
    if cipher_direction == 'decode':
        shifts *= -1
    for i in message:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = position + shifts
            cipher_text += alphabet[new_position]
        else:
            cipher_text += i
    print(f'The {cipher_direction}d text is {cipher_text}')


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(message=text, shifts=shift, cipher_direction=direction)
    check = input('Do you want to go again? yes or no : ')
    if check == 'no':
        should_continue = False
        print('Good Bye !')
