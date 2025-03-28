from ff3 import FF3Cipher

key = "2DE79D232DF5585D68CE47882AE256D6"
tweak = "CBD09280979564"
c = FF3Cipher(key, tweak)
plaintext = "5855380179823966"  # credit card number
ciphertext = c.encrypt(plaintext)
decrypted = c.decrypt(ciphertext)
print(f"{plaintext} -> {ciphertext} -> {decrypted}")
# format encrypted value
ccn = f"{ciphertext[:4]} {ciphertext[4:8]} {ciphertext[8:12]} {ciphertext[12:]}"
print(f"Encrypted CCN value with formatting: {ccn}")
