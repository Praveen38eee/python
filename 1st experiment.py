''' Get an integer input from a user. If the number is odd, then find the factorial of a number and find the number of digits in the factorial of the number. If the number is even, then check if the given number is a palindrome or not.
'''
num = int(input("Enter an integer: "))
if num % 2 != 0:
    factorial = 1
    for i in range(2, num + 1):
        factorial *= i
        num_digits = len(str(factorial))
    print("Factorial:", factorial)
    print("Number of digits in factorial:", num_digits)
else:
    num_str = str(num)
    if num_str == num_str[::-1]:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
