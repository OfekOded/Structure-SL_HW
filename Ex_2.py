# Oded Ofek 215348145
# Ziv Farajun 323920603
import math
import time
from functools import reduce



def Q_1():
    # 1.1
    linear_func = lambda x: x / 2 + 2
    numbers = list(range(10001))
    new_list = list(map(linear_func, numbers))
    print(new_list)
    # 1.2
    print(sum(new_list))
    # 1.3
    total_sum = sum(new_list)
    start_time1 = time.time()
    total_sum = sum(new_list)
    end_time1 = time.time()
    print("Time taken using sum():", end_time1 - start_time1)

    start_time2 = time.time()
    total_sum_imperative = 0
    for num in new_list:
        total_sum_imperative += num
    end_time2 = time.time()
    print("Time taken using imperative method:", end_time2 - start_time2)
    # 1.4
    print(reduce(lambda x, y: x + y, new_list, 0))  # 1.2


def Q_2():
    new_list = list(range(1, 10001))
    odd_num = list(filter(lambda x: x % 2 != 0, new_list))
    print(odd_num)
    even_num = list(filter(lambda x: x % 2 == 0, new_list))
    print(even_num)
    # 2.1
    foo1= lambda x: reduce(lambda z, y: z + y, x[:-1],0)*x[-1]
    foo2= lambda x: reduce(lambda z, y: z + y, x[:-1],0)/2+2+x[-1]
    new_list1=list(map(lambda i: foo1(even_num[:i+1]), range(1, len(even_num))))
    print(new_list1)
    new_list2 = list(map(lambda i: foo2(odd_num[:i + 1]), range(1, len(even_num))))
    print(new_list2)
    print(sum(new_list1))
    print(sum(new_list2))


def Q_3(date,num_dates,day_skip):
    date_components = date.split('/')
    addDays = lambda x: (x + day_skip) % 30
    addMonths = lambda x, y: (y + (x + day_skip) // 30) % 12
    addYears = lambda x, y, z: z + (y + (x + day_skip) // 30) // 12
    dateStr = lambda x, y, z: f"{addDays(x):02}-{addMonths(x, y):02}-{addYears(x, y, z)}"
    print(list(dateStr(int(date_components[0])+i*day_skip,int(date_components[1]),int(date_components[2])) for i in range(num_dates)))


def Q_4_1(exponent):
    return lambda x: pow(x, exponent)


def Q_4_2(num):
    return map(lambda x: Q_4_1(x)(num), range(num))


def Q_4_3(x):
    term_calculator = map(lambda n: Q_4_1(n)(x) / math.factorial(n), range(1000))
    return reduce(lambda a, b: a + b, term_calculator)


def task_manager():
    tasks = {}

    def add_task(task_name, status="incomplete"):
        tasks[task_name] = status

    def get_tasks():
        return tasks

    def complete_task(task_name):
        if task_name in tasks:
            tasks[task_name] = "complete"

    return {
        'add_task': add_task,
        'get_tasks': get_tasks,
        'complete_task': complete_task
    }


if __name__ == '__main__':
    tasks_manager = task_manager()


    tasks_manager['add_task']("Write email")
    tasks_manager['add_task']("Shopping", "in progress")
    tasks_manager['add_task']("Homework")


    current_tasks = tasks_manager['get_tasks']()
    print(current_tasks)


    tasks_manager['complete_task']("Write email")


    current_tasks = tasks_manager['get_tasks']()
    print(current_tasks)


