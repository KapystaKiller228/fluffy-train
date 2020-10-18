import matplotlib.pyplot

def bar_graph(file):
    x_axis = [chr(x) for x in range(ord('a'), ord('z')+1)]
    y_axis = [file.lower().count(x) for x in x_axis]
    matplotlib.pyplot.bar(x_axis, y_axis)
    matplotlib.pyplot.show()

crunch=open('sentence.txt', 'r')
file = crunch.read()
crunch.close()

print('amount of words= %i' % (len(file.split())))
file = file.replace(file.split()[2], file.split()[2][::-1])  #вот эта вот [::-1] это запись наоборот
print(file)
eliF=' '.join(file.split()[::-1]) #строка наоборот
eliF = eliF[0].upper()+ eliF[1::]
print(eliF)

file_new = open('eliF.txt', 'w')
file_new.write(eliF)
file_new.close()

bar_graph(file)