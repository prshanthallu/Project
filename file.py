# def to_weird_case_word(string):
#     #return " ".join(''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(i)])for i in string.split())
#         #                       ' '.join(['ThIs', 'Is', 'A', 'TeSt'])
#     return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate("this")])
# # def to_weird_case(string):
# #     return " ".join(to_weird_case_word(str) for str in string.split())
# print(to_weird_case_word('This is a test'))

# list_1 = [('A', 200), ('B', 400), ('B', 500)]
# dict_1 = dict()
# for student, score in list_1:
#     dict_1.setdefault(student, []).append(score)
# k = [i for i in dict_1.keys()]
# v = [i for i in dict_1.values()]
# for i in v:
#     for j in k:
#         if dict_1[j] == i:
#             print(j, sum(i))
# print(dict_1)
#
# l = ('ARNO', 'ANN'), ('BELL', 'JOHN'), ('CORNWELL', 'ALEX'), ('DORNY', 'ABBA'), ('KERN', 'LEWIS'), ('KORN', 'ALEX'), \
#     ('META', 'GRACE'), ('SCHWARZ', 'VICTORIA'), ('STAN', 'MADISON'), ('STAN', 'MEGAN'), ('WAHL', 'ALEXIS')
# lst = []
# for i in l:
#     for j in i:
#         lst.append(j)
# # lst = map(str, l)
# # line = ",".join(lst)
# # print(line)
# with open("F:\\file.txt", "a+") as myfile:
#     lst = map(str, lst)
#     line = ",".join(lst)+"\n"
#     myfile.write(line)


# defining a decorator
# def hello_decorator(func):
# inner1 is a Wrapper function in
# which the argument is called

# inner function can access the outer local
# functions like in this case "func"
# def inner1():
#     print("Hello, this is before function execution")

# calling the actual function now
# inside the wrapper function.
# func()

# print("This is after function execution")

# return inner1


# defining a function, to be called inside wrapper
# def function_to_be_used():
#     print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behavior
# function_to_be_used = hello_decorator(function_to_be_used)

# calling the function
# function_to_be_used()
from file1 import *

def function():
    e= f()
    return e
def f3():
    f=function()
    return f






f3()
