Q1

tuple = 2, 4, 5, 6, 2, 3, 4, 4, 4, 4
print(tuple)
count = tuple.count(2)
print(count)

Q2


list = [1, 3, 5, 7, 9, 10,21,23]
list[-1:] = [3,4,77,43]
print(list)

Q3


dict1={'name': 'rakesh','rollno': 3516242}
dict2={'class': 'b.tech','college':'TERII'}

dict= dict1.copy()
dict.update(dict2)

print(dict)

  or

def Merge(dict1, dict2):
    return (dict1.update(dict2))

dict1={'name': 'rakesh','rollno': 3516242}
dict2={'class': 'b.tech','college':'TERII'}

print(Merge(dict1, dict2))
print(dict1)


Q4

dict1={'name': 'Manish','rollno': 3516245,'address': 'Kashmir'}
dict2={'class': 'b.tech','college':'TERII','address': 'Jammu'}

for key in dict2:
    if key in dict1:
        dict1[key] = dict2[key] + dict1[key]
    else:
        pass

print(dict1)

Q5

def hello():
    speed = int(input("Enter the speed"))
    birthday = speed + 5
    if (birthday < 60):
      print("No ticket")
    elif (birthday in range(61, 81)):
      print("Small ticket")
    else:
      print("Big ticket")

def hello1():
    speed = int(input("Enter the speed"))
    if (speed < 60):
        print("No ticket")
    elif (speed in range(61, 81)):
        print("Small ticket")
    else:
        print("Big ticket")

while (True):
           birth = input("enter n if your birthday today ")

           if (birth == "n"):
               hello()
               break

           else:
               hello1()
               break

Q6

print('1 for addition')
print('2 for subtraction')
print('3 for multiplication')
print('4 for division')
number=int(input('Choose number'))


if number==1:
    new = int(input('Enter the numbers you want to solve'))

    new9=[input()for i in range(new) ]

    new1=list(map(lambda x : int(x),new9))
    from functools import reduce
#
    addition=reduce(lambda x,y: x+y,new1)
    print('addition is :',addition)
elif number==2:

    new2 = int(input('Enter the numbers you want to solve'))

    new10 = [input() for i in range(new2)]
    new3=list(map(lambda x : int(x),new10))
    from functools import reduce

    subtraction=reduce(lambda x,y: x-y,new3)
    print('subtraction is :',subtraction)
elif number==3:

    new4 = int(input('Enter the numbers you want to solve'))

    new11 = [input() for i in range(new4)]
    new5=list(map(lambda x : int(x),new11))
    from functools import reduce

    multiplication=reduce(lambda x,y: x*y,new5)
    print('multiplication is :',multiplication)
elif number==4:

    new6 = int(input('Enter the numbers you want to solve'))

    new12 = [input() for i in range(new6)]
    new7=list(map(lambda x : int(x),new12))
    from functools import reduce

    division=reduce(lambda x,y: x/y,new7)
    print('division is :',division)
else:
    print('Undefined operation')


Q7

import random
first=int(input("enter the number of elements "))
second=[input("enter from user")for i in range(first)]
print(second)

random.shuffle(second)
print(second)


Q9


tuple_var = (1,2,55,5,"man",36.4,57.9,'false')

print(tuple_var[:10])
print(tuple_var[10])

Q10

a=int(input("enter the first_no:"))
b=a**2
print(b)

