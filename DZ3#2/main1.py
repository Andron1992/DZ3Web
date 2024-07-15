from multiprocessing import Pool, cpu_count
import time
import math

def factors(n):
    result = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            result.append(i)
            if i != n // i:  # щоб уникнути дублювання дільників
                result.append(n // i)
    result.sort()
    return result

def factorize(*numbers):
    num_processes = min(len(numbers), cpu_count())  # Обмеження кількості процесів
    with Pool(processes=num_processes) as pool:
        result = pool.map(factors, numbers)
    return result

if __name__ == '__main__':
    numbers = (128, 255, 99999, 10651060)

    # Перевірка часу виконання паралельної версії
    start_time = time.time()
    a, b, c, d = factorize(*numbers)
    end_time = time.time()

    print(f"Паралельне виконання: {end_time - start_time} секунд")
    print(a)
    print(b)
    print(c)
    print(d)

    # Тестування
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10]
