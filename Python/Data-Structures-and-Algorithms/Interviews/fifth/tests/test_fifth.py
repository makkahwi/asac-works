from fifth.fifth import unique_letters_check
import pytest

# -	Send a string with all-unique letters and expect Boolean value of true to be returned.
# -	Send a string with non-unique letters and expect Boolean value of false to be returned.
# -	Send an empty string and expect an exception error to be returned.


def test_true():
    assert unique_letters_check("hey") == True


def test_false():
    assert unique_letters_check("hello") == False


def test_empty():
    with pytest.raises(Exception):
        unique_letters_check("")
