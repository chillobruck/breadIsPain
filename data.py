import datetime


# определяет количество дней в феврале
def february_days_number():
    year = datetime.date.today().year

    return 29 if year % 4 == 0 else 28


classmates = ['петя', 'маша', 'паша', 'саша', 'вика', 'вероника', 'маруся', 'маркуша', 'крутое имя', 'df', 'dfsa',
              'lol', 'a', 'a']

months = {
    1: 31,
    2: february_days_number(),
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
