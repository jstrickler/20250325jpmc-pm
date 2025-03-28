mary_in = open('DATA/mary.txt')
print(hasattr(mary_in, "__enter__"))
print(hasattr(mary_in, "__exit__"))

# getattr() hasattr() setattr() delattr()

r = getattr(mary_in, "readline")
print(r())

print(dir(mary_in))

class Dog:
    pass

d = Dog()
print(f"{d = }")


def bark(self):
    print("woof! woof!")

setattr(Dog, "wombat", bark)

class GermanShepherd(Dog):
    pass
g = GermanShepherd()

d.wombat()
g.wombat()