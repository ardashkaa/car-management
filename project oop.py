from abc import ABC, abstractmethod
import uuid

class Entity(ABC):
    def __init__(self, name):
        self._id = str(uuid.uuid4())
        self._name = name

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def set_details(self):
        pass

class Showroom(Entity):
    def __init__(self, name):
        super().__init__(name)
        self._location = ""

    def get_details(self):
        print("ID:", self._id)
        print("Name:", self._name)
        print("Location:", self._location)

    def set_details(self):
        try:
            print("======================= *** ENTER SHOWROOM DETAILS *** =======================")
            self._location = input("LOCATION: ")
        except Exception as e:
            print("Error occurred while setting showroom details:", str(e))

class Employees(Entity):
    def __init__(self, name):
        super().__init__(name)
        self._age = 0
        self._department = ""

    def get_details(self):
        print("ID:", self._id)
        print("Name:", self._name)
        print("Age:", self._age)
        print("Department:", self._department)

    def set_details(self):
        try:
            print("======================= *** ENTER EMPLOYEE DETAILS *** =======================")
            self._age = int(input("AGE: "))
            self._department = input("DEPARTMENT: ")
        except ValueError:
            print("Age must be a valid integer.")

class Cars(Entity):
    def __init__(self, name):
        super().__init__(name)
        self._color = ""
        self._fuel_type = ""
        self._price = 0
        self._type = ""
        self._transmission = ""

    def get_details(self):
        print("ID:", self._id)
        print("Name:", self._name)
        print("Color:", self._color)
        print("Fuel Type:", self._fuel_type)
        print("Price:", self._price)
        print("Type:", self._type)
        print("Transmission:", self._transmission)

    def set_details(self):
        try:
            print("======================= *** ENTER CAR DETAILS *** =======================")
            self._color = input("COLOR: ")
            self._fuel_type = input("FUEL TYPE(PETROL/DIESEL): ")
            self._price = int(input("PRICE: "))
            self._type = input("TYPE(SEDAN/SUV/HATCHBACK): ")
            self._transmission = input("TRANSMISSION TYPE(AUTOMATIC/MANUAL): ")
        except ValueError:
            print("Price must be a valid integer.")

def main_menu():
    print()
    print("======================= *** WELCOME TO SHOWROOM MANAGEMENT SYSTEM *** =======================")
    print()
    print("=============================== *** ENTER YOUR CHOICE *** ===============================")
    print()
    print("1].ADD SHOWROOM \t\t\t 2].ADD EMPLOYEE \t\t\t 3].ADD CAR")
    print()
    print("4].GET SHOWROOM \t\t\t 5].GET EMPLOYEE \t\t\t 6].GET CAR")
    print()
    print("=============================== *** ENTER 0 TO EXIT *** ===============================")



def main():
    entities = []
    choice = 100
    while choice != 0:
        main_menu()
        try:
            choice = int(input())
            if choice == 1:
                name = input("Enter Showroom Name: ")
                showroom = Showroom(name)
                showroom.set_details()
                entities.append(showroom)
            elif choice == 2:
                name = input("Enter Employee Name: ")
                employee = Employees(name)
                employee.set_details()
                entities.append(employee)
            elif choice == 3:
                name = input("Enter Car Name: ")
                car = Cars(name)
                car.set_details()
                entities.append(car)
            elif choice == 4:
                print("======================= *** SHOWROOM DETAILS *** =======================")
                for entity in entities:
                    if isinstance(entity, Showroom):
                        entity.get_details()
                        print()
            elif choice == 5:
                print("======================= *** EMPLOYEE DETAILS *** =======================")
                for entity in entities:
                    if isinstance(entity, Employees):
                        entity.get_details()
                        print()
            elif choice == 6:
                print("======================= *** CAR DETAILS *** =======================")
                for entity in entities:
                    if isinstance(entity, Cars):
                        entity.get_details()
                        print()
            elif choice != 0:
                print("Invalid choice. Please enter a valid option.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print("An error occurred:", str(e))

if __name__ == "__main__":
    main()