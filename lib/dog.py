#!/usr/bin/env python3

class Dog:
    approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]

    def __init__(self, name = ''):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        if (type(name) == str) and (1 <= len(name) <= 25):
            print(f"Setting name to {name}")
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed in Dog.approved_breeds:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)


# Dog in dog.py is a class with the name "Dog". .
# Dog in dog.py prints "Name must be string between 1 and 25 characters." if empty string. F
# Dog in dog.py prints "Name must be string between 1 and 25 characters." if not string. F
# Dog in dog.py prints "Name must be string between 1 and 25 characters." if string over 25 characters. F
# Dog in dog.py saves name if string between 1 and 25 characters. .                                                    [ 33%]
# Dog in dog.py prints "Breed must be in list of approved breeds." if not in breed list. F
# Dog in dog.py saves breed if in breed list. .
# Person in person.py is a class with the name "Person". .
# Person in person.py prints "Name must be string between 1 and 25 characters." if empty string. F
# Person in person.py prints "Name must be string between 1 and 25 characters." if not string. F
# Person in person.py prints "Name must be string between 1 and 25 characters." if string over 25 characters. F
# Person in person.py saves name if string between 1 and 25 characters. .
# Person in person.py converts name to title case and saves if between 1 and 25 characters F
# Person in person.py prints "Job must be in list of approved jobs." if not in job list. F
# Person in person.py saves job if in job list. .