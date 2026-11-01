#itertools

from functools import wraps
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

from functools import wraps 
#decorator

import time
def timer(func):
    @wraps(func)
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
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling login")
        print("Arguments:")
        print(args)
        print(kwargs)
        return func(*args, **kwargs)
    return wrapper

@logger
def login(username):
    print(f"User {username} logged in.")    

logged_in = True

def authenticator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if logged_in:
            return func(*args, **kwargs)
        else:
            print("Access denied.")
    return wrapper

@authenticator
def view_profile(username):
    print(f"Viewing profile of {username}")

def uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase
def greet(name):
    return f"Hello, {name}!"

def repeat(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for iteration in range(3):
            func(*args, **kwargs)
    return wrapper

@repeat
def say_hello():
    print("Hello!")


def run_once(func):
    has_run = False
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal has_run
        if not has_run:
            has_run = True
            return func(*args, **kwargs)
        else:
            print("Function has already run.")
    return wrapper

@run_once
def initialize():
    print("Initializing...")


#context manager

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        print("Started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = time.time() - self.start_time
        print(f"Finished in {self.elapsed:.2f} seconds")


with Timer():
    time.sleep(2)
    
from contextlib import contextmanager

@contextmanager
def Database():
    print("Connecting")
    try:
        yield
    finally:
        print("Disconnecting")

with Database() as db:
    print("Performing database operations")

class logger:
    def __enter__(self):
        self.log_file = open("log.txt", "a")
        self.log_file.write("Started\n")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.log_file.write("Finished\n")
        self.log_file.close()

with logger() as log:
    print("Logging operations")


@contextmanager
def Timer():
    start_time = time.time()
    print("Started")
    yield
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Finished in {elapsed_time} seconds")

with Timer():
    time.sleep(2)

#type hints

def multiply(a:int, b:int) -> int:
    return a*b 

class calculator:
    def add(self, a:int, b:int) -> int:
        return a+b
    def divide(self, a:int, b:int) -> float:
        return a/b

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    course: str

stu1= Student("Alice", 20, "Math")
print(stu1)

from typing import TypedDict

class Employee(TypedDict):
    id: int
    name: str
    salary: int

def pay(employee: Employee) -> str:
    print(f"Paying {employee['name']} : id {employee['id']} with salary {employee['salary']}")

def calculate_total(price: float, quantity:int, discount: float) -> float:
    return price * quantity * (1 - discount)

def highest_score(scores: list[int]) -> int:
    return max(scores)

def get_email(user: dict[str, str]) -> str:
    return user["email"]

def search_username(users: list[dict[str, str]], username: str) -> dict[str, str] | None:
    for user in users:
        if user["username"] == username:
            return user
    return None

from typing import TypeVar
T = TypeVar('T')
def double(value: T) -> T:
    return value * 2

from dataclasses import dataclass

@dataclass
class student:
    name: str
    age: int
    course: str
    cgpa: float

stu1 = student("Alice", 20, "Math", 3.8)
print(stu1.name)

stu2 = student("Bob", 22, "Physics", 3.5)
print(stu2.cgpa)

from typing import TypedDict
class movie(TypedDict):
    title: str
    year: int
    rating: float

def print_movie(m: movie) -> None:
    print(f"{m['title']} ({m['year']}) - Rating: {m['rating']}")

from typing import Literal
def chat_mode(mode: Literal["text", "voice"]) -> None:
    if mode == "text":
        print("Text mode activated.")
    elif mode == "voice":
        print("Voice mode activated.")

def logger(value: any)  -> None:
    print(f"Logging value: {value}")

