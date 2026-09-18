import string, secrets, math

def get_password_len():
    while True:
        num = input("Enter desired password length (minimum 8): ").strip()
        try:
            length = int(num)
        except ValueError:
            print("Please enter a whole number.(e.g 4, 15) \n")
            continue

        if length < 8:
            print("For better security, use at least 8 characters (16+ recommended).")
            continue

        return length

def ask_for_symbols(prompt, default = True):
    suffix = "(Y/n): " if default else "(y/N): "
    answer = input(prompt + suffix).strip().lower()
    if answer == "":
        return default
    return answer.startswith("y")

def password_generate(length, use_symbols = True):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    pool = letters + digits
    if use_symbols:
        pool += symbols

    required_chars = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
    ]
    if use_symbols:
        required_chars.append(secrets.choice(symbols))

    remaining_length = length - len(required_chars)
    random_chars = [secrets.choice(pool) for _ in range(remaining_length)]

    password_chars = required_chars + random_chars
    shuffled = shuffle_list(password_chars)

    return ''.join(shuffled)

def shuffle_list(items):
    items = items.copy()
    for i in range(len(items) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        items[i], items[j] = items[j], items[i]
    return items

def estimate_entropy_bits(length, pool_size):
    return round(length * math.log2(pool_size), 1)

def main():
    print("Random Password Generator")

    length = get_password_len()
    use_symbols = ask_for_symbols("Include special characters (!#@$ etc)?", default=True)

    password = password_generate(length, use_symbols=use_symbols)

    pool_size = 52 + 10 + (len(string.punctuation) if use_symbols else 0)
    bits = estimate_entropy_bits(length, pool_size)

    print(f"\nGenerated password: {password}")
    print(f"Length: {length} characters")
    print(f"Estimated entropy: ~{bits} bits of entropy")

if __name__ == "__main__":
    main()