# Wap to check whether an number is prime or compsite

num = int(input("Enter a number: "))

if num == 2:
    print("Prime")
else:
    for i in range(2,num):
        if num % i == 0:
            print("Composite")
            break
    else:
            print("Prime")