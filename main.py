## TASK 1
class ConsoleString:
    def __init__(self):
        self.text = ""

    def get_string(self):
        self.text = input("Enter some text: ")

    def print_string(self):
        print(self.text.upper())


## TASK 2
class Shape:
    def area(self):
        return 0  # По умолчанию фигура не имеет площади


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


sq = Square(10)
print(f"Square area: {sq.area()}")  # 100


## TASK 3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Пример для Rectangle
rect = Rectangle(5, 3)
print(f"Rectangle area: {rect.area()}")  # 15


## TASK 4
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def show(self):
        print(f"x = {self.x}, y = {self.y}")

    def move(self, new_x, new_y):
        self.x, self.y = new_x, new_y

    def distance(self, other_x, other_y):
        print(f"Distance: {((self.x - other_x) ** 2 + (self.y - other_y) ** 2) ** 0.5}")


# Пример для Point
p1 = Point(1, 2)
p1.show()
p1.move(3, 4)
p1.show()
p1.distance(0, 0)


## TASK 5
class Account:
    def __init__(self, owner="", balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("Insufficient funds")
        self.balance -= amount
        return amount


# Пример для Account
acc = Account("Alice", 100)
print(f"Balance before deposit: {acc.balance}")
acc.deposit(50)
print(f"Balance after deposit: {acc.balance}")
acc.withdraw(30)
print(f"Balance after withdrawal: {acc.balance}")


## TASK 6
def filter_primes(numbers):
    return [n for n in numbers if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))]


# Пример для filter_primes
nums = [1, 3, 4, 6, 7, 1, 6, 21, 14, 17, 25, 15, 19]
primes = filter_primes(nums)
print(f"Primes in the list: {primes}")  # [3, 7, 17, 19]
