import logging
from functools import wraps

# import MODULE
# from MODULE import name

logging.basicConfig(
    format="%(levelname)s %(asctime)s %(message)s",
    datefmt="%x-%X",
#    filename="functioncalls.log",
    level=logging.DEBUG
)

def timestamp(f):

    @wraps(f)
    def wrapper(*args, **kwargs):
        logging.debug(f.__name__)
        f_return = f(*args, **kwargs)
        return f_return # call function and return the return value
    return wrapper

@timestamp
def spam() -> int:
    print("spam!!")
    return 100

# spam = timestamp(spam)

print(f"{spam.__name__ = }")

r = spam()  # spam() now calls wrapper(), which calls the original spam()
print(f"{r = }")
spam()
spam()

@timestamp
def ham(count: int) -> None:
    print("ham" * count)

ham(2)
ham(8)
spam()
x = ham(20)
print(f"{x = }")
print(f"{ham.__name__ = }")
print(f"{spam.__name__ = }")

def toast(x: int) -> None:
    print(f"{x = }")

toast(1)
toast(5.6)
toast("abc")

a = 12
b = a
a = 32
