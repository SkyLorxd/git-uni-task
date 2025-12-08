import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функция '{func.__name__}' выполнилась за {execution_time:.10f} секунд")
        return result

    return wrapper


@timer_decorator
def calculate_sum(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


@timer_decorator
def calculate_from_file():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        a = int(lines[0].strip())
        b = int(lines[1].strip())

    result = a + b

    with open('output.txt', 'w') as file:
        file.write(f"Сумма чисел {a} и {b} равна: {result}")

    print(f"{a} + {b} = {result}")


if __name__ == "__main__":
    calculate_sum(12, 17)
    calculate_from_file()