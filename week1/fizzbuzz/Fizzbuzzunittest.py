
def fizzbuzz(input):
    if (input % 5 == 0) and (input % 3 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return  "Fizz"
    if input % 5 == 0:
        return  "Buzz"
    return input


print(fizzbuzz(15))




def get(number):
    if number == 1:
        return  "Get 1"
    elif number == 2:
        return  "Get 2"


print(get(2))