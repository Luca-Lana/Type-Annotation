one_string: str = 'Luca'
one_number: int = 23
one_float_number: float = 23.4
one_boolean: bool = False
one_list: list = [1, 34, 6]
one_tuple: tuple = 1, 23, 4
one_dict: dict = {'name': 'jose', 'age': 23}
one_set: set = {1, 3, 54, 6}

# if i change the value of this variables will work but the libraries together
# with the library will show an error because this is not a good practice


def sum(a: int, b: int, c: float) -> float:  # typing parameters and return

    return a + b + c


# type the list content of list
list_of_int: list[int] = [2, 3, 34, 56, 6]
list_of_string: list[str] = ['asd', 'asdf', 'ewsfp']

# typing dicts
type_dict: dict[str, int] = {
    'A': 2,
    'teste': 23
}

type_dict1: dict[int, list[int]] = {
    123: [2, 34, 78]
}
