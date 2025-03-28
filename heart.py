import random

class Heart:
    def __init__(self):
        self.bpm = 72

    def beat(self):
        print("Lub-dub")
        self.bpm = random.randint(70,75)

    # dunder string method for class, used whenever we need to convert the class into a string
    def __str__(self):
        return f"Heart is beating at {self.bpm} bpm."

    # Dont compare memory addreses, they are the same if the beat at the same beat is what this method does
    def __eq__(self, other):
        return self.bpm == other.bpm