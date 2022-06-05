def run():
    def decorador(func):
        def envoltura():
            print('Esto se añade a mi función original')
            func()
        return envoltura

    def saludo():
        print('!Hola')

    saludo()
    saludo = decorador(saludo)
    saludo()

if __name__ == '__main__':
    run()