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
