import random

class Password_Generator:
    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
       
    def create_password(self):
        self.password_letters = [random.choice(self.letters) for _ in range(random.randint(3,6))]
        self.password_numbers = [random.choice(self.numbers) for _ in range(random.randint(2,3))]
        self.password_symbols = [random.choice(self.symbols) for _ in range(random.randint(4,5))]

        self.password = self.password_letters + self.password_numbers + self.password_symbols

        random.shuffle(self.password)

        return "".join(self.password)