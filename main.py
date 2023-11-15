from typing import List


class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        print("Animal constructor called.")

    def __del__(self):
        print("Animal destructor called.")

    def make_sound(self) -> None:
        pass


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed

    def is_puppy(self) -> bool:
        return self.age < 1

    def display_info(self) -> None:
        print(f"{self.name} is a {self.age}-year-old {self.breed}.")

    def make_sound(self) -> None:
        print("Woof! Woof!")

    def __del__(self):
        print("Dog destructor.")


class Cat(Animal):
    def __init__(self, name: str, age: int, is_indoor: bool):
        super().__init__(name, age)
        self.is_indoor = is_indoor

    def is_kitten(self) -> bool:
        return self.age < 1

    def display_info(self) -> None:
        indoor_status = "indoor" if self.is_indoor else "outdoor"
        print(f"{self.name} is a {self.age}-year-old {indoor_status} cat.")

    def make_sound(self) -> None:
        print("Meow! Meow!")

    def __del__(self):
        print("Cat destructor.")


def main() -> None:
    animals: List[Animal] = [Dog("Hasky", 3, "Labrador"), Cat("Orange", 2, True), Dog("Max", 4, "TestBreed")]

    for animal in animals:
        animal.make_sound()

    # Displaying information
    for animal in animals:
        if isinstance(animal, Dog):
            animal.display_info()
            print(f"Is a puppy: {animal.is_puppy()}")
        elif isinstance(animal, Cat):
            animal.display_info()
            print(f"Is a kitten: {animal.is_kitten()}")

        del animal


if __name__ == "__main__":
    main()
