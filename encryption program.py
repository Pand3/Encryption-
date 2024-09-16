# encryption program 
import random
import string 

 ## list of all characters 
char = " " + string.punctuation + string.ascii_letters + string.digits
char_list = list(char)
key_list = char_list.copy()

## randomly jumble key_list 
random.shuffle(key_list)

## get user message 
user_sentence = input("Sentence: ")


## encrypting message 
encrypted_message = ""
for char in user_sentence:
    index_position =  char_list.index(char)
    encrypted_message += key_list[index_position]
    
print("encryption:", encrypted_message)

#decrypting message
decrypt_message = input("Decrypt message: ")
origional_message = ""
for char in decrypt_message:
    index_position = key_list.index(char)
    origional_message += char_list[index_position]

print("Decrypted message:",origional_message)
            

