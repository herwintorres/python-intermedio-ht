def run():
    def palindrome(string):
        return string == string[::-1]

    print(palindrome('ana'))    

    #funcion anonima
    palindrome_2 = lambda string: string == string[::-1]
    print(palindrome_2('ana'))


if __name__ == '__main__':
    run()