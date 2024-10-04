import pytest
from questions.answer_1 import addNumbers


def test_add_numbers_valid():
    result = addNumbers(2.3499999, 5.7)
    assert result == 8

def test_check_number_in_range():
    with pytest.raises(ValueError) as exc_info:
        addNumbers(0.05,1) 

    assert str(exc_info.value) == "Input numbers must be between 0.1 and 10^6"

def test_check_number_places():
    with pytest.raises(ValueError) as exc_info:
        addNumbers(2.1,2.123456789) 
    
    assert str(exc_info.value) == "Input numbers have at most 8 places after the decimal"