#unión de 2 set
my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}

my_set3 = my_set1 | my_set2
print(my_set3)

#intersección 
my_set4 = my_set1 & my_set2
print(my_set4)

#diferencia
my_set5 = my_set1 - my_set2
print(my_set5)

my_set6 = my_set2 - my_set1
print(my_set6)

#diferencia simétrica
my_set7 = my_set1 ^ my_set2
print(my_set7)