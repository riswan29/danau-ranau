def i_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n%i ==0 :
            return False
        return True

def print_prime(limit):
    for i in range(2, limit):
        if i_prime(i):
            print(i, end=' ')
    print()

print_prime(20)


# for i in range(0,100):
#     if i % 3 == 0 and i % 5 == 0 :
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
