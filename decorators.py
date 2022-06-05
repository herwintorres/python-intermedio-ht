
from datetime import datetime
def run():
    def execution_time(func):
        def wrapper(*args, **kwargs):
            initial_time = datetime.now()
            func(*args, **kwargs)
            final_time = datetime.now()
            time_elapsed = final_time - initial_time
            print("pasaron " + str(time_elapsed.total_seconds()) + " segundos")
        return wrapper
    
    @execution_time
    def randow_func():
        for _ in range(1, 10000000):
            pass
    
    @execution_time
    def suma(a: int, b: int) -> int:
        return a + b
    
    @execution_time
    def saludo(nombre="Cesar"):
        print("Hola " + nombre)

    randow_func()
    suma(8995, 990005)
    saludo("Fscundo")

if __name__ == '__main__':
    run()