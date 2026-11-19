import os

n = int(os.environ["N"])

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")   
elif n % 3 == 0:
    print("Fizz")    
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
    
print("Ejecucion exitosa el numero ingresado era valido")