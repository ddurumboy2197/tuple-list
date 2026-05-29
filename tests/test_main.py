# test_tuple_to_list.py
import pytest
from tuple_to_list import tuple_to_list

def test_empty_tuple():
    assert tuple_to_list(()) == []

def test_single_element_tuple():
    assert tuple_to_list((1,)) == [1]

def test_multiple_element_tuple():
    assert tuple_to_list((1, 2, 3)) == [1, 2, 3]

def test_tuple_with_negative_numbers():
    assert tuple_to_list((-1, -2, -3)) == [-1, -2, -3]

def test_tuple_with_floats():
    assert tuple_to_list((1.5, 2.5, 3.5)) == [1.5, 2.5, 3.5]

def test_tuple_with_strings():
    assert tuple_to_list(('a', 'b', 'c')) == ['a', 'b', 'c']
