
p = 17
q = 23
e = 5

n = p * q 

def char_to_number(char):
    return ord(char.lower()) - ord('a') + 1  

def encrypt(m, e, n):
    return pow(m, e, n)

plaintext = "Truong Tuyet Trinh"
numeric_values = [char_to_number(c) for c in plaintext]  
ciphertext = [encrypt(m, e, n) for m in numeric_values]  

print("P: ", plaintext)
print("C: ", ciphertext)
