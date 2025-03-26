#!/usr/bin/env python
from pytest import fixture

@fixture
def common_fixture():  # user-defined fixture
    return ['alpha', 'beta', 'gamma']


# predefined hook (all hooks start with 'pytest_')
def pytest_runtest_setup(item):
    print(f"{item = }")
    
    if "test_two" in str(item):
        print(f"Hello from setup, {item}", end=" ")
