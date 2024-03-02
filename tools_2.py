import pprint
from datetime import datetime, timedelta
from typing import TypedDict, List

from data import classmates


class Duty(TypedDict):
    date: str
    day_of_week: int
    mates: List[str]


def get_mate():
    now_idx = 0
    while True:
        yield classmates[now_idx]
        now_idx += 1
        if now_idx == len(classmates):
            now_idx = 0


def make_groups_for_month(date=datetime.now().date(), duty_count_for_one=3, nbr_ppl_grp=2):
    mate_generator = get_mate()
    duties_list = []
    group_count = len(classmates) // nbr_ppl_grp + (1 if len(classmates) % nbr_ppl_grp != 0 else 0)

    i = 0

    while len(duties_list) < group_count * duty_count_for_one:
        duty_date = date + timedelta(days=i)
        if duty_date.weekday() == 5 or duty_date.weekday() == 6:
            i += 1
            continue

        mates = []
        for a in range(nbr_ppl_grp):
            mates.append(next(mate_generator))
        i += 1
        duties_list.append(Duty(date=duty_date.strftime("%d.%m.%Y"), day_of_week=duty_date.weekday(), mates=mates))

    pprint.pprint(duties_list)


date = datetime.strptime('01.01.2022', '%d.%m.%Y')

make_groups_for_month(date)
