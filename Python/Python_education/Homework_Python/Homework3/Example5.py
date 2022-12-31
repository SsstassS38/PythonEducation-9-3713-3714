# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


n = int(input('Введите размер числа Фибоначчи '))
if n < 0: n = n*-1
f1 = f2 = 1
list1 = [f1, f2]
for i in range(2, n):
    f1,f2 = f2, f1 + f2
    list1.append(f2)
print(list1)
f1=f2=1
for i in range(-n, 1):
    f1,f2 = f2, f1 - f2
    list1.insert(0, f2)
print(list1)


# n = int(input('Введите количество чисел Фибоначчи в списке: ')) 
 
# def get_fibonacci(n): 
#     fibo_nums = [] 
#     a, b = 1, 1 
#     for i in range(n-1): 
#         fibo_nums.append(a) 
#         a, b = b, a + b                                      №вариант Дениса https://github.com/DenisAFW/Seminar3/blob/master/DZ5.py
#     a, b = 0, 1 
#     for i in range (n): 
#         fibo_nums.insert(0, a) 
#         a, b = b, a - b 
#     return fibo_nums 
 
# fibo_nums = get_fibonacci(n) 
# print(get_fibonacci(n))