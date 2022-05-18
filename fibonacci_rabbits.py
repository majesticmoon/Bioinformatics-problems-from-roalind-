# fibonnaci rabbits

def fibonacci_rabbits(months, offsprings):
    parent, child = 1, 1
    for itr in range(months - 1):
        child, parent = parent, parent + (child * offsprings)
    return child


print(fibonacci_rabbits(5, 3))
