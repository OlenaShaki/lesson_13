import random
import time
from random_word import RandomWords

int_list = []
float_list = []
str_list = []

w = RandomWords()

for i in range(0, 5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(random.uniform(0.1, 100.0))
    str_list.append(w.get_random_word())


def sorting_time(lst, iterations):
    total_time = 0

    for _ in range(iterations):
        start_time = time.time()
        sorted_lst = sorted(lst.values())
        end_time = time.time()

        total_time += end_time - start_time

    average_time = total_time / iterations
    return average_time


iterations = 10
average_time = sorting_time(int_list, iterations)
print(f"Середній час сортування int_list: {average_time} сек")

average_time = sorting_time(float_list, iterations)
print(f"Середній час сортування float_list: {average_time} сек")

average_time = sorting_time(str_list, iterations)
print(f"Середній час сортування str_list: {average_time} сек")