import random


class Password():
    def __init__(self, length=18):
        self.length = length
        self.lower_case = "abcdefghijklmnopqrstuvwxyz"
        self.upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.numbers = "0123456789"
        self.symbols = "@#$&*(){}[]/-_="
        self.allchar = str(self.lower_case) + str(self.upper_case) + str(self.numbers) + str(self.symbols)

    def lower(self):
        return str("".join(random.sample(self.lower_case, self.length)))

    def upper(self):
        return "".join(random.sample(self.upper_case, self.length))

    def number(self, length=10):
        if 3 <= length <= 10:
            return "".join(random.sample(self.numbers, length))
        else:
            raise Exception("Expected range 3 - 10")

    def true_random(self):
        return "".join(random.sample(self.allchar, self.length))


if __name__ == "__main__":
    my_mod = Password()
    print(my_mod.number())
