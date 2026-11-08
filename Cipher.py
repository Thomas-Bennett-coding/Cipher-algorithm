def vigenere(text: str, key: str, decrypt: bool = False) -> str:
    key = [ord(c.lower()) - ord('a') for c in key if c.isalpha() and c.isascii()]
    if not key:
        raise ValueError("Key must contain at least one Latin letter")

    result = []
    i = 0  # advances only on letters
    for ch in text:
        if ch.isascii() and ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = key[i % len(key)] * (-1 if decrypt else 1)
            result.append(chr((ord(ch) - base + shift) % 26 + base))
            i += 1
        else:
            result.append(ch)
    return "".join(result)


key = "secret"
message = input("Enter your WIFI SSID: ")

cipher = vigenere(message, key)
print("Ciphertext:", cipher)
print("Decrypted: ", vigenere(cipher, key, decrypt=True))
