#проверка числа на простоту в is_prime
def is_prime(число):
    for делитель in range(2, int(число**0.5)+1):
        if число % делитель ==0: return False
    return True

print([число for число in range(1, ((int(input('введите верхнюю границу: ')))+1)) if is_prime(число)==True])
