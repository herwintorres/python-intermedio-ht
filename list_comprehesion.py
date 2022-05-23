from numpy import square


def run():
    # squares = []
    # for i in range(1,101):
    #     if i % 3 !=0:
    #         squares.append(i**2)
    #Listas de compresion
    squares = [i**2 for i in range(1,101) if i % 3 != 0]
    print(squares)
    #Diccionarios de compresion de un diccionario
    my_dict = {}
    for i in range(1, 101):
        my_dict[i] = i*3
    print(my_dict)
    #Diccionario de compresión de un diccionario
    my_dict_d = {}
    for i in range(1,101):
        if i % 3 != 0:
            my_dict_d[i] = i**3
    print(my_dict_d)
    #diccionario compresetion de un diccionario
    my_dict_c = {i: i**3 for i in range(1,101) if i % 3 != 0}
    print(my_dict_c)

    


if __name__ == '__main__':
    run()