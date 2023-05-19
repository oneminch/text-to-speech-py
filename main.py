import string
import secrets


class SecretGenerator():

    def __init__(self):
        self.digits = string.digits
        self.special_chars = string.punctuation
        self.lowercase_letters = string.ascii_lowercase
        self.uppercase_letters = string.ascii_uppercase

    def generate_password(self,
                          length: int = 16,
                          alphanumeric_only: bool = False):
        """
        Given a length, generates a strong random password
        """

        if length < 12:
            return "Please enter a password length greater than 10"

        char_types = []

        char_types.append(self.digits)
        char_types.append(self.lowercase_letters)
        char_types.append(self.uppercase_letters)

        if not alphanumeric_only:
            char_types.append(self.special_chars)

        pwd = ""

        for i in range(length):
            # Get random character type from types list
            char_type_index = secrets.choice(range(len(char_types)))

            # Get random character from chosen type
            rand_char = secrets.choice(char_types[char_type_index])

            # Remove character from type to avoid repeated character
            char_types[char_type_index] = char_types[char_type_index].replace(
                rand_char, "")

            # Concatenate character to password string
            pwd += rand_char

        return pwd


def main():
    pwd_length_input = ""

    valid_input = False

    while not valid_input:
        try:
            pwd_length_input = int(
                input("Enter the length of password: (> 12) "))

            if pwd_length_input < 12:
                continue

            valid_input = True
        except ValueError:
            continue

    generator = SecretGenerator()

    pwd = generator.generate_password(pwd_length_input)
    print(f"\nWith Special Character: {pwd}")

    alphanumeric_pwd = generator.generate_password(length=pwd_length_input,
                                                   alphanumeric_only=True)
    print(f"\nWithout Special Character: {alphanumeric_pwd}")


if __name__ == '__main__':
    main()
