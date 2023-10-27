import sys

def read_circle_info(file_path):
    with open(file_path, 'r') as file:
        center_x, center_y = map(float, file.readline().split())
        radius = float(file.readline())
    return center_x, center_y, radius

def point_position(center_x, center_y, radius, point_x, point_y):
    distance = ((point_x - center_x) ** 2 + (point_y - center_y) ** 2) ** 0.5
    if distance == radius:
        return 0  # точка лежит на окружности
    elif distance < radius:
        return 1  # точка внутри окружности
    else:
        return 2  # точка снаружи окружности

def main():
    if len(sys.argv) != 3:
        print("Инструкция: python ваш_скрипт.py file1.txt file2.txt")
        sys.exit(1)

    circle_center_x, circle_center_y, circle_radius = read_circle_info(sys.argv[1])

    with open(sys.argv[2], 'r') as points_file:
        for line in points_file:
            point_x, point_y = map(float, line.split())
            result = point_position(circle_center_x, circle_center_y, circle_radius, point_x, point_y)
            print(result)

if __name__ == "__main__":
    main()

