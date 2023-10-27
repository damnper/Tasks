import sys

# Функция для чтения чисел из файла и возврата их в виде списка
def read_numbers_from_file(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            numbers.append(int(line.strip()))
    return numbers

# Функция для вычисления минимального количества ходов
def min_moves_to_equalize(nums):
    # Вычисляем среднее значение
    average = sum(nums) // len(nums)
    
    # Вычисляем количество ходов, необходимых для приближения всех чисел к среднему значению
    moves = sum(abs(num - average) for num in nums)
    
    return moves

def main():
    if len(sys.argv) != 2:
        print("Инструкция: python ваш_скрипт.py <файл с числами>")
        sys.exit(1)

    filename = sys.argv[1]

    numbers = read_numbers_from_file(filename)
    moves = min_moves_to_equalize(numbers)
    print(moves)

if __name__ == '__main__':
    main()
