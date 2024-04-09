import gnupg

# Initialize GPG object
gpg = gnupg.GPG()

def encrypt_file(input_file, output_file, recipient):
    with open(input_file, 'rb') as f:
        encrypted_data = gpg.encrypt_file(f, recipients=[recipient], output=output_file)
    print('File encrypted successfully.')

def decrypt_file(input_file, output_file, passphrase):
    with open(input_file, 'rb') as f:
        decrypted_data = gpg.decrypt_file(f, passphrase=passphrase, output=output_file)
    print('File decrypted successfully.')

# Example usage
input_file = 'plaintext.txt'
encrypted_file = 'encrypted.txt'
decrypted_file = 'decrypted.txt'
recipient = 'recipient@example.com'
passphrase = 'your_passphrase'

# Encrypt file
encrypt_file(input_file, encrypted_file, recipient)

# Decrypt file
decrypt_file(encrypted_file, decrypted_file, passphrase)
