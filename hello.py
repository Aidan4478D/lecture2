#name = input()
#print(f"Hello, {name}!")


#i = 28
#print(f"i is {i}")

#f = 2.8
#print(f"f is {f}")

#b = False
#print(f"b is {b}")

#n = None
#print(f"n is {n}")

#x = 0

#if x > 0:
    #print("x is positive")
#elif x < 0:
    #print("x is negative")
#else:
    #print("x is zero")

#name = "Alice"
coordinates = (10.0, 20.0)
names = ["Alice", "Bob", "Charlie"]
coordinates[0]

for i in range(5):
    print(i)

for name in names:
    print(name)

if coordinates[0] == 10:
    print("x is positive")


s = set()
s.add(1)
s.add(3)
s.add(5)
s.add(3)
print(s)

if s == 3:
    print("s is positive")



ages = {"Alice": 22, "Bob": 27}
ages["Charlie"] = 30
ages["Alice"] += 1

print(ages)


def square(x):
    return x * x

def main():
    for i in range(10):
        print("{} squared is {}".format(i, square(i)))

if __name__ == "__main__":
    main()

from hello import square

print(square(10))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3,5)
print(p.x)
print(p.y)
