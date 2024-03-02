from tools import *

while True:
    match input('Что вы хотите сделать? L - вывести лист с одноклассниками в соответсвие с данными; Q - выйти').lower():
        case 'l':

            print(add_days_in_loop((int(input('Дата')),
                                    int(input('Месяц')),
                                    int(input('День недели'))),
                                   int(input('Кол-во повторов'))))
        case 'q':
            break
