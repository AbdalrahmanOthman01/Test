# # print("Hello python") #This is the comment for this line 

# # # to create a var we can make it like that 
# # a = 5
# # b = 5.5
# # o = 5j + 3
# # i = range(8)
# # x = "hello"
# # g = "h"
# # n = 'Hello'
# # j = 'h'
# # l = True
# # k = False
# # m = []
# # v = {}
# # p = frozenset(v)
# # y = ()
# # r = {3,}
# # u = {"hi":"hello"}
# # e = None

# # print(type(e))

# # x = []
# # x.insert(0,"Apple")
# # x.insert(4,"Ap")
# # print(x)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# thislist = ["apple", "banana"]
# print(mylist)

# class myClass:
#     x = 6
# p1 = myClass

# print(p1.x)

# class Person:
#   def __init__(theClass, name, age):
#     theClass.name = name
#     theClass.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Person("John", 36)

# print(p1)

# mystr = "banana"
# myit = iter(mystr)
# print(myit)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

def myFunc():
  print("Hello")

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi , 256)
c = np.sin(x)
plt.plot(x, c)
plt.show()
