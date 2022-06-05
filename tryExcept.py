def run():
    def palindrome(string):
        return string == string[::-1]
    
    try:
        print(palindrome(1))
    except TypeError:
        print("Solo se puede ingresar string")

if __name__ == '__main__':
    run()