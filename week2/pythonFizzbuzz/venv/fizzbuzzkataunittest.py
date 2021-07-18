def fizzbuzz(number):
    number = int(input('Enter a number: '))


    while number:
        if (number % 5 == 0) and (number % 3 == 0):
            return "FizzBuzz"
        if number % 3 == 0:
            return "Fizz"
        if number % 5 == 0:
            return "Buzz"
    return number

print(fizzbuzz('number'))
# print(fizzbuzz(6))
# print(fizzbuzz(10))
# print(fizzbuzz(15))

# ----------------------------------------------------------------------------------------------------- #

def get(n):
    n = int(input('Enter a number: '))
    
    while n:
        if n == 1:
            return "Get 1"
        if n == 2:
            return "Get 2"
        if (n != 1) and (n != 2):
            break
    return n 

print(get('n'))
# print(get(1))
# print(get(2))
