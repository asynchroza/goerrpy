from decorators import goerr

@goerr
def larger_than_five(number_one):
    if number_one > 5:
        return number_one
    else:
        raise Exception('Number is too small')

value, err = larger_than_five(int(input()))

if err != None:
    print(err)
else:
    print(value)


