'''3.	Countdown Iterator
Create a class called countdown_iterator. Upon initialization it should receive a count. Implement the iterator, so it returns each number
of the countdown (from count to 0 inclusive).
Note: Submit only the class in the judge system
'''

class countdown_iterator():

    def __init__(self, count):
        self.count = count
        self.index = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        index = self.index
        self.index -=1
        return index


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
