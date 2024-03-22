import random
import string

def generate_password(length=12, num_upper=4, num_lower=4, num_digits=2, num_special=2):
    if length < num_upper + num_lower + num_digits + num_special:
        raise ValueError("Password length should be greater than the sum of specified character counts.")
    
    upper_chars = ''.join(random.choice(string.ascii_uppercase) for _ in range(num_upper))
    lower_chars = ''.join(random.choice(string.ascii_lowercase) for _ in range(num_lower))
    digit_chars = ''.join(random.choice(string.digits) for _ in range(num_digits))
    special_chars = ''.join(random.choice(string.punctuation) for _ in range(num_special))

    remaining_length = length - (num_upper + num_lower + num_digits + num_special)
    all_chars = upper_chars + lower_chars + digit_chars + special_chars
    remaining_chars = ''.join(random.choice(all_chars) for _ in range(remaining_length))

    password = ''.join(random.sample(all_chars + remaining_chars, length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the length of the password: "))
    upper_count = int(input("Enter the number of uppercase letters: "))
    lower_count = int(input("Enter the number of lowercase letters: "))
    digit_count = int(input("Enter the number of digits: "))
    special_count = int(input("Enter the number of special characters: "))

    generated_password = generate_password(password_length, upper_count, lower_count, digit_count, special_count)
    print("Generated Password:", generated_password)