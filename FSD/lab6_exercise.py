import sys

print("welcome, argument available are 1 and 2")

if sys.argv[1] == "1":
    class Person:
        def __init__(self):
            self.name = input("Enter name: ")
            self.age = int(input("Enter age: "))
            self.index = 0
            self.index += 1
        def display(self):
            print(f"{self.index} Name: {self.name}\nAge: {self.age}")

    class People:
        def __init__(self):
            self.people = []
        def show(self):
            for person in self.people:
                person.display()
        def add(self):
            self.people += [Person()]
        def update(self):
            index = int(input("Enter the index of the person to update: "))
            self.people[index] = Person()
        def main():
            people = People()
            people.show()
            while True:
                print("\n1. Add person")
                print("2. Update person")
                print("3. Display people")
                print("4. Exit\n")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    people.add()
                elif choice == 2:
                    people.update()
                elif choice == 3:
                    people.show()
                elif choice == 4:
                    break
                else:
                    print("\nInvalid choice!\nPlease enter a valid choice! (1/2/3/4):")
    if __name__ == "__main__":
        People.main()

elif sys.argv[1] == "2":
    print("helo")

else:
    "please enter a valid argument!! (1/2)"

