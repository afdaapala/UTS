import random
import sys

def exercise1():
    def calculateCircle(radius):
        area = 3.14 * radius * radius
        perimeter = 2 * 3.14 * radius
        volume = (4/3) * 3.14 * radius * radius * radius
        return area, perimeter, volume
    radius = int(input("Enter the radius: "))
    calculateCircle(radius)
    print(calculateCircle(radius)[0])
    print(calculateCircle(radius)[1])
    print(calculateCircle(radius)[2])

def exercise2():
    def random20array():
        for i in range(20):
            print(random.randint(1, 100), end = " ")
    random20array()
    
exercise2()