from pprint import pprint  # import prettyprint function

# global variables
COUNT = 42  
ANIMAL = 'Wombat'

def spam(fruit):  # function parameters are local
    # global foo # BAD BAD BAD
    knight = 'Lancelot'  # local variable
    print("Locals:")
    pprint(locals())  # locals() returns dict of all locals
    print()
    def ham():
        print("ham locals:", locals())
        print("HAM!")
        # knight is nonlocal
    return ham

h = spam('mango')
h()
# globals() returns dict of all globals
print("Globals:")
pprint(globals())
print()

g = globals()
g['color'] = "blue"  # create a new variable
print("color:", color)

print(f"{ANIMAL = }")
g['ANIMAL'] = 'possum'
print(f"{ANIMAL = }")
