'''06. Fibonacci Generator
Create a generator function called fibonacci() that generates the Fibonacci numbers infinitely (starting from 0). Each Fibonacci number is
created by the sum of the current number with the previous.
Note: Submit only the function in the judge system
'''

def fibonacci():
    fi_number = 1
    fi_previous = 0
    counter = 1
    while True:

        if counter == 1:
            yield fi_previous
            counter +=1
        elif counter == 2:
            yield fi_number
            counter +=1
        else:
            sum_feb = fi_previous + fi_number
            yield sum_feb
            fi_previous = fi_number
            fi_number = sum_feb




generator = fibonacci()
for i in range(6):
    print(next(generator))
