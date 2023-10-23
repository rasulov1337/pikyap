import random


# Пример:
# gen_random(5, 1, 3) должен выдать выдать 5 случайных чисел
# в диапазоне от 1 до 3, например 2, 2, 3, 2, 1
# Hint: типовая реализация занимает 2 строки
def gen_random(num_count, begin, end):
    random.seed()

    for _ in range(num_count):
        yield random.randint(begin, end)


if __name__ == 'main':
    a = gen_random(5, 1, 3)
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
