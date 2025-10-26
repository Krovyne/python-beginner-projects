print("=== Odd or Even checker ===")
num = int(input("Please input number = "))

#using modulo for checking the remainder of the number when divided by two
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
