from datetime import datetime
def run():
    my_time = datetime.now()
    print(my_time)
    # my_day = datetime.date.today()
    # print(my_day)
    my_str = my_time.strftime('%d/%m/%Y')
    print(f'Formato LATA: {my_str}')

    my_str = my_time.strftime('%m/%d/%Y')
    print(f'Formato USA: {my_str}')

    my_str = my_time.strftime('Estamos en el año %Y')
    print(f'Formato Random: {my_str}')

if __name__ == '__main__':
    run()