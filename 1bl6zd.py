import random, numpy

def random_array():
    return [random.random() for i in range(10)]

array = random_array()
print('Array of 10 random numbers = %s\nMinimal element = %s\nMaximal element = %s\nAverage value = %s\nStandard deviation = %s\nFifth element = %s\nAverage of the previous 5 numbers = %s' % (array, numpy.min(array), numpy.max(array), numpy.mean(array), numpy.std(array), array[5], (numpy.min(array) + numpy.max(array) + numpy.mean(array) + numpy.std(array) + array[5]) / 5))
#В массиве номера элементов начинаются не с 1, а с 0, поэтому 5 элемент это не array[5], а array[4], как с порядком этажей в германии