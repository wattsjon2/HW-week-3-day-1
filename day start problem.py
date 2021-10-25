# check if a random int is odd or even. If even return fizz, if odd return buzz

def fizzBuzz(randInt):
    if randInt % 2 == 1:
        return("Buzz")
    else:
        return("Fizz")

print(fizzBuzz(6))