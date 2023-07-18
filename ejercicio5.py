

# ejercicio 5
limite = 100000

fibonacci_anterior = 0
fibonacci_actual = 1

print(fibonacci_anterior)

while fibonacci_actual < limite :
    print(fibonacci_actual)    
    # 0,1,1,2,3, .....

    fibonacci_siguiente = fibonacci_anterior + fibonacci_actual

    fibonacci_anterior = fibonacci_actual

    fibonacci_actual = fibonacci_siguiente