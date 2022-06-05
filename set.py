my_set = {1, 2, 3, 4, 5, 6}
#set vacío
empty_set = set()
#convertir una lista en un set
my_list = [1, 1, 2, 3, 4, 4, 5]
my_set_list = set(my_list)
print(my_set_list)
#convertir una tupla en un set
my_tuple = ("Hola", "Hola", "Hola", 1)
my_set_tupla = set(my_tuple)
print(my_set_tupla)
#añadir un elemento
my_set_tupla.add(5)
print(my_set_tupla)
#añadir multipes elementos
my_set_list.update([7, 8, 9, 10])
print(my_set_list)
my_set_list.update((11, 12, 13), {14, 15})
print(my_set_list)
#borrar un elemento del set discard
my_set_list.discard(15)
print(my_set_list)
#borrar un elemento del set remove
my_set_list.remove(14)
print(my_set_list)
#borrar un elemento aleatorio 
my_set_list.pop()
print(my_set_list)
#limpiar el set
my_set_list.clear()
print(my_set_list)

