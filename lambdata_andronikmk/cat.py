"""
Simple cat class
"""

class Cat:

    # class attribute
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def multiply_cats(self, name):
        numbers = self.name * 10
        print(numbers)
