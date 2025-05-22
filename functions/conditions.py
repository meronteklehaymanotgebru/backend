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

def countdown(start):
    while start!=0:
     print(start)
     start-=1

def countdown_with_break(start,stop):
    while(start>0):
        print(start)
        if(start==stop):
            break
        start-=1


def swap_list(listnums):
    x=len(listnums)
    i=listnums[0]
    j=x-1
    while(i<j):
        temp=i
        listnums[i]=listnums[j]
        j=temp
        i+=1
        j+=1
    print(listnums)
swap_list()

def countdown_with_continue(start):
    while start>0:
        if start%2==0:
            start-=1
            continue
        print(start)
        start-=1