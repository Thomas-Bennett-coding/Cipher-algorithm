def vigenere(text: str, key: str, decrypt: bool = False) -> str:
    shifts = []
    for c in key:
        if c.isascii() and c.isalpha():
            shifts.append(ord(c.lower()) - ord('a'))
        elif c.isascii() and c.isdigit():
            shifts.append(int(c))
    if not shifts:
        raise ValueError("Key must contain at least one Latin letter or digit")

    result = []
    i = 0
    for ch in text:
        shift = shifts[i % len(shifts)] * (-1 if decrypt else 1)
        if ch.isascii() and ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
            i += 1
        elif ch.isascii() and ch.isdigit():
            result.append(str((int(ch) + shift) % 10))
            i += 1
        else:
            result.append(ch)
    return "".join(result)


key = "secret"
message = input("Enter net ID: ")

cipher = vigenere(message, key)
print("Ciphertext:", cipher)
print("Decrypted: ", vigenere(cipher, key, decrypt=True))
