def collatz(number):
    if number%2==0:
        num = number//2
        print(num)
        return num
    else:
        num = 3 * number + 1
        print(num)
        return num

num = 0
while num!=1:
    number = int(input("Enter the number: "))
    num = collatz(number)
