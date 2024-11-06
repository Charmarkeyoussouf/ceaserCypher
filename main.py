def encrypt_caesar_cipher(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        # Encrypt uppercase letters
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char  # Non-alphabetic characters stay the same
    return encrypted_text

def decrypt_caesar_cipher(cipher_text, shift):
    decrypted_text = ""
    for char in cipher_text:
        # Decrypt uppercase letters
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase letters
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

# Example usage
shift_key = 3  # Example shift key
plain_text = "Hello, World!"
encrypted_text = encrypt_caesar_cipher(plain_text, shift_key)
print(f"Encrypted Text: {encrypted_text}")

decrypted_text = decrypt_caesar_cipher(encrypted_text, shift_key)
print(f"Decrypted Text: {decrypted_text}")
