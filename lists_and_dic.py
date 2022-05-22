def run():
    my_list = [1, "Hello", True,4.5]
    my_dict = {"firname":"Facundo", "lastname":"Garcia"}

    super_list = [
        {"firname":"Facundo", "lastname":"Garcia"},
        {"firname":"Miguel", "lastname":"Torres"},
        {"firname":"Pepe", "lastname":"Rodelo"},
        {"firname":"Susana", "lastname":"Martinez"},
        {"firname":"José", "lastname":"Garcia"}
    ]

    super_dict ={
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums":[-1, -2, 0, 1, 2],
        "floating_nums":[1.1, 4.5, 6.43]
    }

    #recorrerla lista 
    for key, value in super_dict.items():
        print(key, "-", value)
if __name__ == '__main__':
    run()