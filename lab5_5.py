#!/usr/bin/env python3

number = int(input("Input number: "))

if number > 1:
    i = 2
    while i != number:
        if (number % i) == 0:
            print("Is not a prime number")
            break
        i += 1
    else:
        print("Is a prime number")
else:
    print("Is not a prime number")
