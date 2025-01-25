import random


class TestException(Exception):
    pass

def func():
    print("func works")
try:
    try:
       func()
    except TestException as e:
       raise e
       print("A")
    finally:
       print("B")
except Exception as e:
    print("C")  
finally:
    print("D")

#1. func works
#2. B
#3. D
"""
надо сделать метод, который принимает отсортированный массив
 и отдает отсортированный массив квадратов по возрастанию
"""

not_srtf_mas = [1,43,2,55,-3]
def func2(massive:list)->list:
    #new = []
    #for el in massive:
        #new.append(el**2)
    return sorted(map(lambda x:x**2,massive))

print(func2(not_srtf_mas))