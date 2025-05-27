def square(number):
    print(number*number)

def add(x,y):
    result=x+y
    return result

def multiply(w,u):
    result=x*y
    return result


def divide(x,y):
    result=x/y
    return result
def substract(x,y):
    result=x-y
    return result

def exponent(x,y):
    result=x**y
    return result

def modulus(x,y):
    result=x%y
    return result

def substract(x,y):
    result=x%y
    return result

def sum(*numbers):
    sum=0
    for i in numbers:
        sum+=i
    print(sum)


# when we access them they will be put in a tuple that is why we are iterating

def divisible_by_seven_five(num):
    if num in range(1500,2701):
        if(num % 7==0 and num%5==0):
            print(num)
        else:
            print(f"{num} not divisible by 5 and 7")
    else:
        print(f"{num} is not in the range")

def diamond():

    rows = 5  # Number of rows for the widest part

 # Upper part
    for i in range(1, rows + 1):
      for j in range(i):
          print("*", end=" ")
      print()

 # Lower part
    for i in range(rows - 1, 0, -1):
        for j in range(i):
           print("*", end=" ")
        print()

def selam():
    stari = []
    for i in range(6):
        stari.append("*")
        print(stari)
    for i in range(6):
        stari.pop()   # pop removes the last element
        print(stari)
selam()







    