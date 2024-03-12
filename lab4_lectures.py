import sys
import math as m


name = input("Student name: ")
mark = int(sys.argv[1])

if mark >85:
    grade ="HD"
elif mark >= 75:
    grade = "D"
elif mark > 65:
    grade = "C"
elif mark > 50:
    grade="p"
else:
    grade = "2"
print(f'{name} mark is {mark} and grade is {grade}')

n = int(input("n = "))

for e in range(1,n+1):
    f=1
    for i in range(1,e+1):
        f *= i
    print(f'Factorial({e}) = {f}')
print()
for e in range(1,n+1):
    print(f'Factorial({e}) = {m.factorial(e)}')
    

rain = int(input("Rain: "))

count = 0

maximum=sys.maxsize

while rain != -1:
    if rain == 0:
        count += 1
    else:
        maximum = max(count, maximum)
        count=0
    rain = int(input("Rain: "))
maximum = max(maximum, count)
print(f"Longest dry spell = {maximum}")

s = input("String: ")

while s != "*":
    total = 0
    for c in "aeiou":
        frequency = s.lower().count(c)
        total += frequency
        print(f'{c}-> {frequency:03}')
    print(f"Total vowels = {total}")
    s = input("String: ")

