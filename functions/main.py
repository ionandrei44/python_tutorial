say = print
say("Test")


def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello(func):
    text = func("Hello")
    print(text)


hello(loud)
hello(quiet)


def divisor(x):
    def dividend(y):
        return y / x

    return dividend


divide = divisor(2)
print(divide(10))


def double(x):
    return x * 2


print(double(5))

double2 = lambda x: x * 2
multiply = lambda x, y: x * y
full_name = lambda first_name, last_name: first_name + " " + last_name
age_check = lambda age: True if age >= 18 else False


print(double2(6))

print(multiply(5, 5))

print(full_name("First", "Name"))

print(age_check(18))
