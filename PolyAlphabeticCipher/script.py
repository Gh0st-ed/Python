class PolyAlphabeticCipher:
    def __init__(self, key):
        self.key = key

    def clean_text(self, text):
        # Odstranění přebytečných znaků
        # Remove unnecessary characters
        cleaned_text = ''.join(char.lower() for char in text if char.isalpha())
        return cleaned_text

    def transform(self, text, encrypt=True):
        # Šifrování a dešifrování textu
        # Encrypting and decrypting text
        text = self.clean_text(text)
        result = []

        for i, char in enumerate(text):
            shift = ord(self.key[i % len(self.key)]) - ord('a')
            if encrypt:
                # Posun znaku
                # Shift the character
                transformed_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                # Zpětný posun
                # Reverse shift
                transformed_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            result.append(transformed_char)

        return ''.join(result)


def encrypt_file(input_filename, output_filename, key):
    # Šifrování souboru
    # Encrypting the file
    cipher = PolyAlphabeticCipher(key)
    with open(input_filename, "r", encoding="utf-8") as file:
        plaintext = file.read()
        encrypted_text = cipher.transform(plaintext, encrypt=True)

    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(encrypted_text)


def decrypt_file(input_filename, output_filename, key):
    # Dešifrování souboru
    # Decrypring the file
    cipher = PolyAlphabeticCipher(key)
    with open(input_filename, "r", encoding="utf-8") as file:
        ciphertext = file.read()
        decrypted_text = cipher.transform(ciphertext, encrypt=False)

    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(decrypted_text)


def main():
    # Klíč
    # Key
    key = "ASDFGHJKLPOIUZTREWQYXCVBNM"

    # Šifrování
    # Encryption
    encrypt_file("plaintext.txt", "encrypted.txt", key)

    # Dešifrování
    # Decryption
    decrypt_file("encrypted.txt", "decrypted.txt", key)

if __name__ == "__main__":
    main()
