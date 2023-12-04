
from application.salary import calculate_salary
from application.db.people import get_employees
from tqdm import tqdm
import time
import datetime

if __name__ == '__main__':

    print(f'Дата время вызова функции calculate_salary {datetime.datetime.today()}')
    calculate_salary()
    print(f'Дата время вызова функции get_employees {datetime.datetime.today()}')
    get_employees()

    mylist = [1, 2, 3, 4, 5, 6, 7, 8]
    for i in tqdm(mylist):
        time.sleep(1)