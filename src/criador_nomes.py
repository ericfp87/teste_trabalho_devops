import random


class RandomNames:
    def generate_name(self):
        names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
        return random.choice(names)

    def generate_surname(self):
        surnames = ['Smith', 'Johnson', 'Brown', 'Taylor', 'Miller']
        return random.choice(surnames)
