import threading
import time
import random

data_list = [random.randint(1,3) for _ in range(70000000)]

def data_change(data):
    for i in range(len(data)):
        if data[i] == 2 or data[i] == 3:
            data[i] = 1
    return data

def data_thread_change(data,func, num_threads = 2):

    part = len(data) // num_threads
    # тут ділиться довжина листа на кількість потоків, щоб потім надати кожному потоку рівну частину данних для обробки.

    is_there_some = len(data) % num_threads 
    # Ця змінна існує на випадок якщо дата не ділиться на рівні частини.

    
    parts = [data[i * part : (i + 1) * part] for i in range(num_threads)]
    # Цей список створюється задля того, аби передавати рівно поділені частини данних у потоки.
    # Приклад, якщо потоків 2 а лист з данними має 100 значеннь воно має видавати [data[0,50],data[50:100]] 
    
    if is_there_some != 0:
        parts[-1] += data[num_threads * part : num_threads * part + is_there_some]
    # Якщо дата не ділиться на рівні частини, то цей іф блок додає залишок до останнього потоку який ми запускатимемо. 

    threads = [] 
    results = [] 
    for i in range(num_threads):
        t = threading.Thread(target=lambda x: results.append(func(x)), args=(parts[i],))
        # Ця лямбда потрібна для того щоб ми могли витягнути результати з потоків. 
        # Лямбда бере аргси і передає їх в ікс, після чого виконує функцію функ і апендить результати.
        # Приклад як лябда виглядатиме у першому потоці якщо ми розділяємо на два потоки і маємо лист на 100 значеннь:
        # lambda data[0,50]: results.append(func(data[0,50]))

        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    sorted_data = []
    for result in results:
        sorted_data.extend(result)

    return sorted_data


# тестую в мультипотоці

time_start1 = time.time()

c = data_thread_change(data_list,data_change, 2)

time_finish1 = time.time()
print(f"speed with multithreading: {time_finish1-time_start1}")

# тестую без мультипотоку

time_start2 = time.time()

b = data_change(data_list)

time_finish2 = time.time()
print(f"speed without multithreading: {time_finish2-time_start2}")

print(c==b) # перевіряю чи данні збігаються. 

# Дивна річ в тому, що якщо я використовую 2 потоки, я можу виграти секунду-півтори часу, але якщо я збільшую кількість потоків
# то перевага зменшується.

# Приклад моїх результатів з 2 потоками:
#  speed with multithreading: 6.219631195068359 
#  speed without multithreading: 8.0895094871521

# Приклад моїх результатів з 4 потоками:
#  speed with multithreading: 6.531551122665405
#  speed without multithreading: 7.699871301651001

# Приклад моїх результатів з 8 потоками:
#  speed with multithreading: 6.84086799621582
#  speed without multithreading: 7.21393895149231