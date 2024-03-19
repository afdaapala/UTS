def number1():
    name = input("Enter your name: ")
    while (name != "*"):
        print("Hello", name)
        name = input("Enter your name: ")

#recursive methods
def number2():
    def factorial(x):
        return 1 if (x == 1 or x ==0) else x * factorial(x - 1)
    print(factorial(5))
    
def number3():
    def isPrime(n, i = 2):
        if (n <= 2):
            return True if (n == 2) else False
        if (n % i == 0):
            return False
        if (i * i > n):
            return True
        return isPrime(n, i + 1)
    print(isPrime(int(input("enter a number: "))))
    
number3()