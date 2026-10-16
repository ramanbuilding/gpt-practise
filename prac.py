#itertools

from itertools import count

c = count(100,5)
print(next(c))
print(next(c))
print(next(c))  

from itertools import cycle
cy= cycle(["❤️","💙"])

for i in range(6):
    print(next(cy))

from itertools import repeat
r = repeat("Hello",3)
for i in r:
    print(i)

from itertools import chain
c1 = [1,2,3]
c2 = ["a","b","c"]
for i in chain(c1,c2):  
    print(i)


from itertools import islice
c3 = count(10)
print(list(islice(c3, 5)))

from itertools import product
for i in product([1,2],["a","b"]):
    print(i)

letters = ['A', 'B', 'C']
for i in product(letters, repeat=2):
    print(i)

from itertools import permutations
for i in permutations([1,2,3]):
    print(i)

from itertools import combinations
for i in combinations([1,2,3] ,2):
    print(i)

from itertools import accumulate
for i in accumulate([1,2,3,4]):
    print(i)

from itertools import groupby
animals = ['cat', 'cat', 'bird', 'dog', 'cat']
for key, group in groupby(animals):
    print(key, list(group))

def password_gen(letters, length):
    for p in product(letters, repeat=length):
        yield "".join(p)

for password in password_gen("abc", 2):
    print(password)

numbers= count(0)
for i in islice(numbers, 20):
    print(i)

light= cycle(["Red","Yellow","Green"])
for i in range(9):
    print(next(light))

l1=["A","B","C"]
l2=[1,2,3]
l3=[True,False]
for i in chain(l1,l2,l3):
    print(i)

letters = "AB"
for i in product(letters, repeat=3):
    print("".join(i))


print("Permutations")
for i in permutations(["A","B","C"], 2):
    print(i)

print("Combinations")
for i in combinations(["A","B","C"], 2):
    print(i)

numbers = [10, 20, 30, 40]
for i in accumulate(numbers):
    print(i)


#decorator

import time
def timer(func):
    def wrapper(*args, **kwargs):
        print("Starting...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Finished in {end_time - start_time} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Function complete.")

slow_function()

def logger(func):
    def wrapper(username):
        print("Calling login")
        print("Arguments:")
        print(username)
        return func(username)
    return wrapper

@logger
def login(username):
    print(f"User {username} logged in.")    

login("Alice")