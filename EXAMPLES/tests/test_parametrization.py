import pytest
from types import NoneType
from datetime import datetime

def triple(x):  # Function to test
    return x * 3

test_data = [(5, 15), (0, 0), (-1, -3), ('a', 'aaa'), ([True], [True, True, True])]  # List of values for testing containing input and expected result

@pytest.mark.parametrize("input,result", test_data)  # Parametrize the test with the test data; the first argument is a string defining parameters to the test and mapping them to the test data
def test_triple(input, result):  # The test expects two parameters (which come from each element of test data)
    print("input {} result {}:".format(input, result))  # The test expects two parameters (which come from each element of test data)
    assert triple(input) == result   # Test the function with the parameters

import os
import sqlite3

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
president_db_path = os.path.join(THIS_DIR, 'presidents.db')

db_conn = sqlite3.connect(president_db_path)  # open relative to EXAMPLES
db_cursor = db_conn.cursor()
db_cursor.row_factory = sqlite3.Row  # set the row factory to be a Row object

db_cursor.execute('select birthdate, deathdate from presidents')
presidents =  db_cursor.fetchall()

@pytest.mark.parametrize('dob,dod', presidents)
def test_pres_dates(dob, dod):
    assert isinstance(dob, str)
    assert isinstance(dod, (str, NoneType))