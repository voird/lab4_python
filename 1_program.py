#По каналу связи передаётся последовательность целых чисел - показания
#прибора. В течение N минут (N – натуральное число) прибор ежеминутно
#регистрирует значение силы тока (в условных единицах) в электрической сети
#и передаёт его на сервер. Определите три таких переданных числа, чтобы
#между моментами передачи любых двух из них прошло не менее К минут, а
#произведение этих чисел было максимально возможным. Запишите в ответе
#остаток от деления найденного произведения на 10^6 + 1

def find_max_product(N, K, values):
    max_product = float('-inf')

    for i in range(N - 2):
        for j in range(i + K, N - 1):
            for k in range(j + K, N):
                product = values[i] * values[j] * values[k]
                max_product = max(max_product, product)

    return max_product % (10**6 + 1)

def main():
    # Чтение данных из файла A
    with open("D:/лабораторные работы по питону/4/27-168a.txt", "r") as file_a:
        N_a, K_a = map(int, file_a.readline().split())
        values_a = [int(file_a.readline().strip()) for _ in range(N_a)]

    result_a = find_max_product(N_a, K_a, values_a)

    # Чтение данных из файла B
    with open("D:/лабораторные работы по питону/4/27-168b.txt", "r") as file_b:
        N_b, K_b = map(int, file_b.readline().split())
        values_b = [int(file_b.readline().strip()) for _ in range(N_b)]

    result_b = find_max_product(N_b, K_b, values_b)

    print(result_a, result_b)

if __name__ == "__main__":
    main()
