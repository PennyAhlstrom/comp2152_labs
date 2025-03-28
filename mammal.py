# So we don't need to refer to heart by heart.Heart we import like this
from heart import Heart
# instead of like this
#import heart

# Mammal HAS a heart

class Mammal:
    def __init__(self, age):
        self.age = age
        self.heart = Heart() # Creates a heart object, assigned to the heart property

    def speak(self):
        print("Grr...")

    # Double circle red arrow up means overrides methods in object - object is?
    def __str__(self):
        return f"Mammal is {self.age} years old."