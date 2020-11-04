'''05.Take halves
You are given a skeleton with the following code:

def solution():
    def integers():
        # TODO: Implement

    def halves():
        for i in integers():
            # TODO: Implement

    def take(n, seq):
        # TODO: Implement

    return (take, halves, integers)


Implement the three generator functions:
•	integers() - generates an infinite amount of integers (starting from 1)
•	halves() - generates the halves of those integers (each integer / 2)
•	take(n, seq) - takes the first n halves of those integers
Note: Complete the functionality in the skeleton and submit it in the judge system


'''

def solution():
    def integers():
        number = 1
        while True:
            yield number
            number +=1

    def halves():
        for i in integers():
            yield i/2

    def take(n, seq):
        numbers = []
        integer_halves = halves()
        for i in range(n):
            numbers.append( next(seq))
        return numbers

    return (take, halves, integers)

#inteters_gen = integers()
#integer_halves = halves()
#interer_take = take()

#for i in range(5):
#    print(next(inteters_gen))
   # print(next(integer_halves))
    #print(next(integer_halves))
take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
