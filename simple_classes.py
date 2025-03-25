import sqlite3

#  list, tuple, bytes, str  are all array-like types

# x = [1, 2, 3]   list
# x = 1, 2, 3  tuple
# x = b"123"  bytes
# x = "123"    str

# instance = ClassName()

colors = []  # colors = list()
colors.append('green')
colors.insert(0, 'black')
colors.append('yellow')

x = 5  # x = int(5)

db_conn = sqlite3.connect('wombats.db')

print(f"{type(sqlite3) = }")
print(f"{type(colors) = }")
print(f"{type(x) = }")
print(f"{type(db_conn) = }")

class Dog:
    # instance method
    def pant(self):
        print("pant pant pant")

    @classmethod
    def open_kennel(cls):
        pass

    # d.open_kennel()
    # Dog.open_kennel()

    @staticmethod
    def bark(bark_type):
        print(f"{bark_type}! {bark_type}!")

d1 = Dog()
d2 = Dog()
d1.bark("woof")
d2.bark("yip")  # Dog.bark(d2, "yip")

