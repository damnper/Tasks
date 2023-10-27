import sys

def circular_path(n, m):
    if n < 1 or m < 1:
        print("n и m должны быть больше или равны 1")
        sys.exit(1)

    circle = list(range(1, n + 1))
    hashmap = set()
    path = []

    pointer = 1
    first_element = 1
    last_element = 0
    
    while first_element not in hashmap:
        pointer -= 1
        interval = []
        for i in range(m):
            if pointer >= n:
                pointer = 0
            
            interval.append(circle[pointer])
            pointer += 1
        
        path.append(interval)
        
        last_element = int(path[-1][-1])
        hashmap.add(last_element)
        
    return [str(path[j][0]) for j in range(len(path))]

def main():
    if len(sys.argv) != 3:
        print("Инструкция: python ваш_скрипт.py n m")
        sys.exit(1)
    else:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        print("".join(circular_path(n, m)))

if __name__ == "__main__":
    main()