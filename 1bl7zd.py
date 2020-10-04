import random

def random_array(i):
    return [random.random() for i in range(i)]

def complex_random_array(i):
    return [(random.randint(0,10)+1j*random.randint(0,10)) for i in range(i)]

def random_length_array(i):
    return [str(random.randint(0,120)) for i in range(i)]

array=random_array(10)
complex_array=complex_random_array(8)
length_array=random_length_array(9)
cortage=[]
cortage.extend([array,complex_array,length_array])
cortage=tuple(cortage)

print('исходный массив - ', array)
print('по возрастанию', sorted(array))
print('\nисходный комплексный массив - ', complex_array)
print('комплексныые по возрастанию модулю', sorted(complex_array, key=abs))
print('комплексныые по убыванию вещ части', sorted(complex_array, key=lambda x: x.real, reverse=True))
print('\nисходный массив с разными длиннами элементов- ', length_array)
print('по возрастанию длины', sorted(length_array, key=len))
print('по лексикографическому порядку', sorted(length_array, key=str.lower))
print('\nисходный кортеж =', cortage)
print('кортеж, сортированный по возрастанию длины строк',sorted(cortage,key=len))