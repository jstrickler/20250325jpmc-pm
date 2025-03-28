

class Dog:
    def __call__(self):
        print("woof! woof!")

    def doit(self):
        print("doing it")
d = Dog()
d()
d()
d.doit()