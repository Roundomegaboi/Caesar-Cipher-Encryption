#simple caesar cipher
#imports
from random import randint

#functions
def encrypt(key, message,reverse=False):
    new_message = ''
        
    for letter in message:
        new_val = ord(letter) + key if not reverse else ord(letter) - key
        
        #cycle characters round if overflow (only use ascii characters)
        if new_val > 126: 
            new_val = 32 + (new_val - 127)
        elif new_val < 32:
            new_val = 126 - (31 - new_val)
            
        new_char = chr(new_val)
        new_message += new_char
    
    return new_message
    

def convert_key(key) -> int:
    #converts the users entered key into a usuable format
    if key.isalpha():
        key = key[0]
        key = ord(key)
    else:
        key = int(key)
    
    if key > 94:
        key = key % 94 #get remainder after dividing by total number of chars availible for this caesar cipher

    return key

#main
print('Encrypt (1)')
print('Decrypt (2)')
print('Print Test Cases (3)')
user_choice = input()

if user_choice == '1' or user_choice.lower() == 'encrypt':
    print('Enter the string you wish to encrypt: ')
    user_string = input()
    
    print('Enter key you wish to encrypt it with: ')
    user_key = input()
    user_key = convert_key(user_key)
    
    encrypted_user_string = encrypt(user_key, user_string)
    print(f'Your encrypted string is: \'{encrypted_user_string}\'')

elif user_choice == '2' or user_choice.lower() == 'decrypt':
    print('Enter the string you wish to decrypt: ')
    user_string = input()
    
    print('Enter key you wish to decrypt it with: ')
    user_key = input()
    user_key = convert_key(user_key)
    
    decrypted_user_string = encrypt(user_key, user_string, reverse=True)
    print(f'Your decrypted string is: \'{decrypted_user_string}\'')

elif user_choice == '3':
    sentences = ['Hello World',
                 'The Quick Brown Fox Jumped Over the Lazy Dog',
                 'ABCDEFGhijklmnOPQRSTUVwxyZ',
                 'Why did the chicken cross the road???',
                 'That is great!',
                 '123 x 456 = 56088',
                 'I said \'Why so serious?\'',
                 'Alan Turing (1912-1954) was a great computer scientist',
                 'My email is example@gmail.co.uk']
    
    print('9 Test Cases:\n')
    for sentence in sentences:
        key = randint(1,100)
        print(f'Sentence before encryption: {sentence}')
        sentence_encrypted = encrypt(key,sentence)
        print(f'Sentence after encryption (key={key}): {sentence_encrypted}')
        print(f'Sentence after decryption: {encrypt(key, sentence_encrypted, reverse=True)}')
        print()