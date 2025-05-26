from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

def encrypt(string):
    return pow(bytes_to_long(string.encode()), e, N)

def decrypt(c):
    return long_to_bytes(pow(c, d, N))


with open("flag.txt", "r") as flagFileHandle:
    FLAG = flagFileHandle.read().strip()

p, q = getPrime(512), getPrime(512)
N = p*q
e = 65537
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)


encrypted_flag = encrypt(FLAG)


print("[!] Encrypted flag:", encrypted_flag)
print("Note: For encryption the plaintext will be first converted to hex and then encrypted")

while True:
    print("\n1) Encrypt Plaintext")
    print("2) Decrypt Cipher")
    print("[?] Enter your choice: ")
    choice = input()

    if choice == "1":
        print("\n[?] Enter text to encrypt: ")
        text = input()
        print("[+] Plaintext (hex):", text.encode().hex())
        print("[+] Encrypted text:", encrypt(text))

    elif choice == "2":
        try:
            print("\n[?] Enter text to decrypt: ")
            text = int(input())
            decrypted = decrypt(text)
            decrypted_hex = decrypted.hex()
            try:
                decrypted_ascii = decrypted.decode('latin-1', errors="ignore")
            except:
                decrypted_ascii = "[-] Unable to convert to ASCII"

            if decrypted_ascii.startswith("HOOT{"):
                print("[-] TRY HARDER NOOBS!!")
            else:
                print("[+] Decrypted text (hex):", decrypted_hex)
                print("[+] Decrypted text (ASCII): ", decrypted_ascii)
        except:
            print("[-] Invalid ciphertext.")

    else:
        print("[-] Invalid option selected")
