# Задание 3.

def multiple():
    multiples = [n for n in range(20,240) if n % 20 == 0 or n % 21 == 0]

    return multiples


print(f'Числа кратные 20 или 21: {multiple()}.')
