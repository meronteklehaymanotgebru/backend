def check_if_even(num):
    if num%2==0:
        print(f"{num} is even")

def check_even_or_odd(num):
     if num%2==0:
        print(f"{num} is even")
     else:
        print(f"{num} is odd")


def divisiblity_check(n):
    for i in range(1,n+1):
        if i%2==0:
            print(f"{i} is divisible by 2")
        elif i%3==0:
            print(f"{i} is divisible by 3")
        elif i%5==0:
            print(f"{i} is divisible by 5")
        else:
            print(f"{i} is not divisible by 2,3 or 5")