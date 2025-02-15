
L = ['T', 'R', 'U', 'O', 'N', 'G', 'T', 'U', 'Y', 'E', 'T', 'T', 'R', 'I', 'N', 'H']
k = 17
ciphertext = []

for char in L:
    if 'A' <= char <= 'Z':
        new_char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
        ciphertext.append(new_char)
    else:
        ciphertext.append(char)

ciphertext = ''.join(ciphertext)
print("Ciphertext:", ciphertext)
