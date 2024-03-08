"""
Atividade 03 - Trabalho sobre Thread

Elaborar um programa em Python ou C# que calcule vários números fatoriais:
O programa deve inicialmente perguntar ao usuário a quantidade de cálculos a serem realizados;
Para cada cálculo o programa deve perguntar ao usuário um número;
Em seguida, o programa deve iniciar uma thread para cada cálculo, calculando os respectivos fatoriais dos números informados;
Cada thread deve ter um nome único e deve exibir seu nome junto com a iteração no cálculo do fatorial, mostrando a iteração e o cálculo da iteração. Ao final do cálculo, exibir o resultado do fatorial.
Exemplo de uma thread calculando o fatorial de 5:

Thread 3 - Iniciou
Thread 3 - 5 (cálculo iteração: 5)
Thread 3 - 4 (cálculo iteração: 20)
Thread 3 - 3 (cálculo iteração: 60)
Thread 3 - 2 (cálculo iteração: 120)
Thread 3 - Resultado 120
"""
import threading

def factorial_calculated(number, thread_name):
    print(f"{thread_name} - Iniciou")
    factorial = 1
    for i in range(1, number+1):
        print(f"{thread_name} - {i} (cálculo iteração: {factorial})")
        factorial *= i
    print(f"{thread_name} - Resultado: {factorial}")

amounts = int(input("Quantos números fatoriais deseja calcular? "))


for i in range(1, amounts+1):
    number = int(input(f"Digite o {i}º número: "))
    thread = threading.Thread(target=factorial_calculated, args=(number, f"Thread {i}"))
    thread.start()

print("Todos os cálculos foram iniciados!")
