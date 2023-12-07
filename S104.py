def decorator_uppercase(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@decorator_uppercase
def quote1():
    return 'Teamwork makes the dream work'

@decorator_uppercase
def quote2():
    return 'Work smarter, not harder'

if __name__ == '__main__':
    print(quote1())
    print(quote2())


