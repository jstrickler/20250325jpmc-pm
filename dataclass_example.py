from dataclasses import dataclass

@dataclass
class Person:
    first_name: str
    last_name: str

p1 = Person("Bugs", "Bunny")
p2 = Person("Elmer", "Fudd")

for p in p1, p2:
    print(p.first_name, p.last_name)

print(f"{p1 = }")
