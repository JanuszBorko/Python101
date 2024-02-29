class Animal:
    def __init__(self, kind, name, legs) -> None:
        self.kind = kind
        self.name = name
        self.legs = legs

    # def __str__(self) -> str:
    #     print(f"Your {self.kind} is named {self.name}")

    def speak(self, sound):
        print(f"hago este sonido: {sound}")
              
class Dog(Animal):
    def __init__(self, kind, name, legs, color) -> None:
        super().__init__(kind, name, legs)
        self.color = color

    def bite(self, strenght):
        print(f"Dog bites you wiht {strenght} strenght")

    def __str__(self, ) -> str:
        return super().__str__()

class Cat(Animal):
    def __init__(self, kind, name, legs, eyes) -> None:
        super().__init__(kind, name, legs)
        self.eyes = eyes

    def balance(self):
        print("Cat is balance master")

###--------main-----
        
animal = input("What animal do you have (Dog / Cat): ")
match animal.upper():
    case "DOG":
        name = input("what's your dog's name: ")
        color = input("What's its color: ")
        dog = Dog("mammal", name, 4, color)
        print(dog)
        dog.speak("Bark")
    case "CAT":
        pass
    case _:
        print("this animal is not set")






