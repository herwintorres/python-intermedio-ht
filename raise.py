def run():
    def palindrome(string):
        try:
            if len(string) == 0:
                raise ValueError("No se le puede ingresar una cadena vacia")
            return string == string[::-1]
        except ValueError as ve:
            print(ve)
            return False
    try:
        print(palindrome(""))
    except TypeError:
        print('Solo se pueden ingresar string')
if __name__ == '__main__':
    run()