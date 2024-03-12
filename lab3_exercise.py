import math
import sys

## number 1
x = 4
y = 2
print("x + y = ", x+y)
print("x - y = ", x-y)
print("x / y = ", x/y)
print("x * y = ", x*y)
print("x % y + x / y = ", x%y+x/y)
print("(y^7 + 7 / (sqrt(5) + x)) * x^4 % 5 + 2 = ", (math.pow(y,7) + 7/(math.sqrt(5)+x))*(x**4%5+2))

## number 2
# x = input("input  x value:")
# y = input("input  y value:")
print(int(x))
print(int(y))
z = math.pow(x,y)
print(z)
result = math.sqrt(z)
print(result)
print(f'{z:.2f} \n{result:.2f}')

## number 3

radius = int(input("enter the radius : "))
area = math.pi * math.pow(radius, 2)
volume = 4/3 * math.pi * math.pow(radius, 3)
print('the radius is "', radius, '", the area is "', area, '"')
print('the radius is "', radius, '", the area is "', volume, '"')

## number 4
Ax= int(input("please enter the x1 of A : "))
Ay= int(input("please enter the y1 of A : "))
Bx= int(input("please enter the x2 of B : "))
By= int(input("please enter the y2 of B : "))
distance = math.sqrt((Bx-By)**2+(By-Ay)**2)
print(distance)

## number 5
aString = input("please enter a string : ")
print("the first character is ", aString[0])
print("the last character is ", aString[len(aString)-1])
print("the lowercase : ", str.lower(aString))
print("the string length : ", len(aString))

## number 6

class Car:
    def __init__(self, make, pos) -> None:
        self.make = make
        self.pos = pos
    def move(self, pos):
        self.pos =+ pos
    def description(self):
        return f"{self.make} is at position {self.pos}"
        # return '{} and {}'.format(self.make, )

typeCar = Car("BMW", 0)

print(typeCar.description())
typeCar.move(15)
print(typeCar.description())

## number 7
n = int(input("enter the size element : "))
numbers = [0] * n
print(numbers)
numbers[0] = 10
print(numbers[0])
numbers[len(numbers)-1]=-5
print(numbers[len(numbers)-1])
numbers[int(len(numbers)/2)]=3
print(numbers[int(len(numbers)/2)])
print(numbers)