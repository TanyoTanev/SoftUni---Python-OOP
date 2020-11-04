'''1. Take Skip
Create a class called take_skip. Upon initialization it should receive a step (number) and a count (number).
Implement the __iter__ and __next__ functions. The iterator should return the count amount of numbers (starting from 0) and with
the given step. For more clarification, see the examples:
Note: Submit only the class in the judge system
'''

class take_skip():

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_number >= self.count:
            raise StopIteration
        current_number =self.current_number
        self.current_number += 1
        return self.step * current_number


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
