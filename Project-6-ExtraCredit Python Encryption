alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567891011"

user_input = input("Enter a secret message: ")

encrypt = ""
decrypt = ""

# To Encrypt
for i in user_input:
    place_holder = alphabet.index(i)
    new_position = alphabet[place_holder + 5]
    encrypt += new_position
print(encrypt)

# To Decrypt
for j in encrypt:
    place_holder = alphabet.index(j)
    old_position = alphabet[place_holder - 5]
    decrypt += old_position
print(decrypt)
