import data
from data import *

last_day_of_weak = None
last_day = None
last_month = None


# разделяет общий список одноклассников на группы, чтобы потом можно было приписать к этим группам даты
def make_groups(nbr_ppl_grp=2):
    list = data.classmates
    new_list = []
    person = 0

    for i in range(len(list) // nbr_ppl_grp):
        new_list.append([])
        for a in range(nbr_ppl_grp):
            new_list[i].append(list[person + a])
        person += nbr_ppl_grp

    if len(list) % nbr_ppl_grp != 0:
        new_list.append([])
    for i in range(len(list) % nbr_ppl_grp):
        new_list[-1].append(list[person + i])
    return new_list


on_duty_list_with_groups = make_groups()


# приписывает даты к группам
def add_days(first_day, month, day_of_weak_of_first_day):
    """    global next_date
    global next_month
    global next_day_of_weak"""

    global on_duty_list_with_groups

    date_list = []
    day_of_the_weak = day_of_weak_of_first_day
    extra_days, counter = 0, 0

    for _ in range(len(on_duty_list_with_groups)):
        date = first_day + counter + extra_days
        counter += 1

        if date > months.get(month):
            date, extra_days, counter = 1, 0, 2
            month += 1
            first_day = 0
        date_list.append((date, month, day_of_the_weak))

        if day_of_the_weak == 4:
            extra_days += 2
            day_of_the_weak = 0
        else:
            day_of_the_weak += 1

    return date_list, [date, month, day_of_the_weak - 1 if day_of_the_weak != 0 else 4]


def add_days_in_loop(last_date, repeating_number):
    full_date_list = []
    full_list = []
    for _ in range(repeating_number):
        classmates_groups = make_groups()
        date_list, last_date = add_days(last_date[0], last_date[1], last_date[2])

        for i in zip(date_list, classmates_groups):
            full_list.append(i)

        if last_date[2] > 4:
            last_date[2] = 0
            last_date[0] += 3
        else:
            last_date[0] += 1
            last_date[2] += 1

    return list(full_list)

# TODO Иправить баг выше.
