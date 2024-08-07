#!/usr/bin/python3
# Python program to display all the prime numbers within an interval

#Desde que numero cuenta los numeros primos
lower = 1
#Hasta que numero cuenta los numeros primos
upper = 100

print("Los numeros primos entre", lower, "y", upper, "son los sig.:")

#Recorre num desde lower hasta upper de uno en uno
for num in range(lower, upper + 1):
   
   #Chequea que en la primera ejecucion num sea mayor a 1
   #Todos los numeros primos son mayores que 1
   if num > 1:
       
       # Revisa si el numero es diviisble por algun numero menor asi mismo
       for i in range(2, num):
           if (num % i) == 0: #Si es divisible no es primo
               break
       else: # Si no es divisible es primo
           print(num)
