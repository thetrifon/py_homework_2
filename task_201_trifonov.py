#1. Создать список и заполнить его элементами различных типов данных. 
#Реализовать скрипт проверки типа данных каждого элемента. 
#Использовать функцию type() для проверки типа. 
#Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [6, 5.4, "list_content", None, True] #внес элементы в список
for i in my_list:
    print(f'{i} is {type(i)}') #скрипт для проверки типа данных
