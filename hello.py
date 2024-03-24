
def hello_world():
    return "Hello, World!"


def concatenate_strings(str1, str2):
    return str1+str2


def add_integers(num1, num2):
    return num1+num2


def multiply_integers(num1, num2):
    return num1*num2


def create_list(element1, element2, element3):
    return [element1, element2, element3]


def create_dictionary(key1, value1, key2, value2):
    return {key1: value1, key2: value2}


# Tests
def run_tests():
    assert hello_world() == "Hello, World!", "hello_world function should return 'Hello, World!'"
    assert concatenate_strings(
        "Hello", "World") == "HelloWorld", "concatenate_strings function should concatenate two strings."
    assert add_integers(
        5, 3) == 8, "add_integers function should add two integers."
    assert multiply_integers(
        5, 3) == 15, "multiply_integers function should multiply two integers."
    assert create_list("a", "b", "c") == [
        "a", "b", "c"], "create_list should create a list with three elements."
    assert create_dictionary("key1", "value1", "key2", "value2") == {
        "key1": "value1", "key2": "value2"}, "create_dictionary should create a dictionary with two key-value pairs."

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
