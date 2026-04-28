def prime_checker(number):
    for i in range(2, number):          # Checa se o numero pedido é divisivel por todos ate chegar nele mesmo, comeca por 2 pq tudo é divisivel por 1
        if (number % i) == 0:
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is a prime number")


n = int(input())
prime_checker(number = n)