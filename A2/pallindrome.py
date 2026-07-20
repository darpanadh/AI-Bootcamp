# To check where a number is palindrome or not

num = int(input("Enter a number :"))

n = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num//10

if  n == rev:
    print("Palindrome")
else:
    print("Not palindrome")