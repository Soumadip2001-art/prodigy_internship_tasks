def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? (Q to quit): ").upper()
        if choice == 'Q':
            break
        elif choice in ['E', 'D']:
            message = input("Enter your message: ")
            while True:
                try:
                    shift = int(input("Enter the shift value (a positive integer): "))
                    if shift >= 0:
                        break
                    else:
                        print("Shift value should be a positive integer.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
            
            if choice == 'E':
                result = encrypt(message, shift)
                print(f"Encrypted message: {result}")
            else:
                result = decrypt(message, shift)
                print(f"Decrypted message: {result}")
        else:
            print("Invalid choice. Please enter 'E' to encrypt, 'D' to decrypt, or 'Q' to quit.")

if __name__ == "__main__":
    main()
