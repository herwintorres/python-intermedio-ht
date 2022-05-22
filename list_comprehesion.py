from numpy import square


def run():
    # squares = []
    # for i in range(1,101):
    #     if i % 3 !=0:
    #         squares.append(i**2)
    #Listas de compresion
    squares = [i**2 for i in range(1,101) if i % 3 != 0]
    print(squares)
    #Diccionarios de compresion
    my_dict = {}
    for i in range(1, 101):
        my_dict[i] = i*3
    print(my_dict)


if __name__ == '__main__':
    run()