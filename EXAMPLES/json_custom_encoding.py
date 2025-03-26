import json
from datetime import date

class Parrot():  # sample user-defined class (not JSON-serializable)
    def __init__(self, name, color):
        self._name = name
        self._color = color

    @property
    def name(self):  # JSON does not understand arbitrary properties
        return self._name

    @property
    def color(self):
        return self._color

parrots = [  # list of Parrot objects
    Parrot('Polly', 'green'),  #
    Parrot('Peggy', 'blue'),
    Parrot('Roger', 'red'),
]



data = {  # dictionary of arbitrary data
    'spam': [1, 2, 3],
    'ham': ('a', 'b', 'c'),
    'toast': date(2014, 8, 1),
    'parrots': parrots,
}

def encode(obj):  # custom JSON encoder function
    # structured pattern matching
    match obj:  # added in 3.11
        case date():
            return obj.ctime()
        case Parrot():
            return obj.__dict()
        case _:
            return obj

    # if isinstance(obj, date):  # check for date object
    #     return obj.ctime()  # convert date to string
    # elif isinstance(obj, Parrot):  # check for Parrot object
    #     return obj.__dict__ # {'name': obj.name, 'color': obj.color}  # convert Parrot to dictionary
    # return obj  # if not processed, return object for JSON to parse with default parser

# convert Python data to JSON data;
# 'default' parameter specifies function for custom encoding;
# 'indent' parameter says to indent and add newlines for readability
print(json.dumps(data, default=encode, indent=4))
