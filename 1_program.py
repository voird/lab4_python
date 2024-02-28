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
