from decorators import goerr
import typing


@goerr()
def get_numbers_larger_than_five(list: typing.List):
    result = []
    for num in list:
        if type(num) is not int:
            raise Exception("All values should be numbers!")

        if num > 5:
            result.append(num)

    return result


value, err = get_numbers_larger_than_five([4, 5, 6, 7])

if err is not None:
    print(err)

print(value)  # [6, 7]


"""If you need to decorator to unpack the return values of your function, you may pass the unpack argument"""  # noqa: E501


@goerr(unpack=True)
def get_numbers_smaller_than_five_but_unpack(list: typing.List):
    result = []
    for num in list:
        if type(num) is not int:
            raise Exception("All values should be numbers!")

        if num < 5:
            result.append(num)

    return result, result  # so that it can be unpacked


first_list, second_list, err = get_numbers_smaller_than_five_but_unpack([3, 4, 5, 7])

if err is not None:
    print(err)

print(
    f"First list is {first_list} and second list is {second_list}"
)  # First list is [3, 4] and second list is [3, 4]


@goerr()
def test_exception():
    raise Exception("ERROR")

value, err = test_exception()

if err is not None:
    print(err)