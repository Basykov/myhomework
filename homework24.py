import time
import multiprocessing

# Define global locks
file_lock = multiprocessing.Lock()


def generate_file_1(name=str):
    with file_lock:
        with open(name, "w") as fileop:
            gen = (str(i*10) for i in range(1, 5000001))
            fileop.write("\n".join(gen))

def generate_file_2(name=str):
    with file_lock:
        with open(name, "w") as fileop:
            gen = (str(i*2) for i in range(1, 6000001, 2))
            fileop.write("\n".join(gen))

def reading(file=str, start_line=int, num_lines=int):
    lines = []
    with file_lock:
        with open(file, 'r') as fileop:
            for i in range(start_line - 1):
                fileop.readline()
            for i in range(num_lines):
                line = fileop.readline().strip()
                if not line:
                    break
                lines.append(line)
    return lines

if __name__ == '__main__':
    # Test with multiprocessing

    start = time.time()

    process1_1 = multiprocessing.Process(target=generate_file_1, args=("practice1.txt",))
    process1_2 = multiprocessing.Process(target=generate_file_1, args=("practice1.txt",))
    process2_1 = multiprocessing.Process(target=generate_file_2, args=("practice2.txt",))
    process2_2 = multiprocessing.Process(target=generate_file_2, args=("practice2.txt",))
    process3_1 = multiprocessing.Process(target=reading, args=("practice1.txt", 1, 500000,))
    process3_2 = multiprocessing.Process(target=reading, args=("practice1.txt", 500000, 1000000,))
    process4_1 = multiprocessing.Process(target=reading, args=("practice2.txt", 1, 250000,))
    process4_2 = multiprocessing.Process(target=reading, args=("practice2.txt", 250000, 500000,))

    process1_1.start()
    process1_2.start()
    process2_1.start()
    process2_2.start()
    process3_1.start()
    process3_2.start()
    process4_1.start()
    process4_2.start()

    process1_1.join()
    process1_2.join()
    process2_1.join()
    process2_2.join()
    process3_1.join()
    process3_2.join()
    process4_1.join()
    process4_2.join()

    end = time.time()
    print(end - start)
    
    # Test without multiprocessing

    start = time.time()

    generate_file_1("practice1.txt")
    generate_file_1("practice1.txt")
    reading("practice1.txt", 1, 1000000)
    generate_file_2("practice2.txt")
    generate_file_2("practice2.txt")
    reading("practice2.txt", 1, 500000)

    end = time.time()
    print(end - start)