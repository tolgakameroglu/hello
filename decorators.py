""" def announce(f):
    def wrapper():
        print("1111")
        f()
        print("2222")
    return wrapper

@announce
def hello():
    print("Hello world !")

hello() """

""" people = [
    {"name":"neso","okul":"mkp iio"},
    {"name":"ipo","okul":"bhyal"},
    {"name":"nazo","okul":"okyanus"}
]


#def f(person):
#    return person["name"]

people.sort(key=lambda person : person["name"])

print(people) """

import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("value error")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("error divide by 0.")
    sys.exit(1)

print(f"{x} / {y} = {result}")
