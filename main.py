class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Animal constructor called.")

    def __del__(self):
        print("Animal destructor called.")

    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def __del__(self):
        print("Cat destructor.")

    def make_sound(self):
        print("Woof! Woof!")


class Cat(Animal):
    def __init__(self, name, age, is_indoor):
        super().__init__(name, age)
        self.is_indoor = is_indoor

    def __del__(self):
        print("Cat destructor.")

    def make_sound(self):
        print("Meow! Meow!")


def main():
    array_size = 3
    animals = []

    animals.append(Dog("Buddy", 3, "Labrador"))
    animals.append(Cat("Whiskers", 2, True))
    animals.append(Dog("Max", 4, "German Shepherd"))

    for animal in animals:
        animal.make_sound()

    # Виведення результатів
    for animal in animals:
        del animal


if __name__ == "__main__":
    main()
