import datetime
from tqdm import tqdm
from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    current_date = datetime.datetime.now().date()
    print(f'Today is {current_date}!')

    for i in tqdm(range(5)):
        get_employees(i)

    calculate_salary()