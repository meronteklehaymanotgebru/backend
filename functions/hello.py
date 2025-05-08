def hello():
    print("Hello AkiraChix")

# -m for modules while running it starts reading from the top
# python3 -m file name  this is called feeding the code to pour interpreter
# Importing first to interpreter, check the path then 'from module import function'
# From hello import hello// Either no output or an error
# Then you call the function in interpreter
# if we were in functions directory we would say from functions import hello
def say_hello(name):
    print(f"hello {name}")
def hello_student(name,age):
    year=2025-age
    print(f"Hello {name}, born in {year}")

def my_country(name="Ethiopia"):
    print(f"I love my country {name}")

def hello_students(*students):
    for student in students:
        print(f"Hello {student}")

def welcome_student(**kwarys):
    name=kwarys.get("name","stranger")
    age=kwarys.get("age","Undefined")
    country=kwarys.get("country","Unknown country")
    # for i in kwarys.values:
    #     if i=="Ethiopia":
    print(f"{name} from {country}, your age is {age}")
        #    print("She is fasting")


def stats(*args, **kwargs):
    print(args)
    print(kwargs)

