from functools import reduce
#función de compresión
my_list = [1, 4, 5, 6, 9, 13, 19, 21]
# odd = [i for i in my_list if i % 2 != 0]
#uso con filter
odd = list(filter(lambda x: x%2 != 0, my_list))
print('Filter = ',odd)

#list compresion
my_list2 = [1, 2, 3, 4, 5]
squares = [i**2 for i in my_list2]
print('list = ',squares)

#uso de map
squares2 = list(map(lambda x: x**2, my_list2))
print('map = ',squares2)

#multiplicar una lista
my_list3 = [2, 2, 2, 2, 2]
all_multiplied = 1
for i in my_list3:
    all_multiplied = all_multiplied * i
print(all_multiplied)

#uso de reduce 
all_multiplied2 = reduce(lambda a, b: a * b, my_list3 )
print(all_multiplied2)

#Ejercicio reduce
my_list4 = [2, 3, 4, 5, 6, 8]
all_multiplied3 = reduce(lambda a, b: a+b, my_list4)
print("Suma del vector 3: ",all_multiplied3)
