def outer_function():
    print('''Assign task to student''')

    task = 'Read Python book chapter 3.'
    def inner_function():
        print(task)
    return inner_function

homework = outer_function()
homework()

# A function can be passed to another function as an argument.
def friendly_reminder(func):
    '''Reminder for husband'''
    func()
    print('Don\'t forget to bring your wallet!')

def action():
    print('I am going to the store buy you something nice.')

friendly_reminder(action)

"""
I am going to the store buy you something nice.
Don't forget to bring your wallet!
"""

from datetime import datetime

def log_datetime(func):
    '''Log the date and time of a function'''
    print("checking.......")
    def wrapper():
        print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-"*30}')
        func() # call daily_backup inside code....
    return wrapper

"""
x=log_datetime(daily_backup)
x()
"""
@log_datetime
def daily_backup():
    print('Daily backup job has finished.')   
daily_backup() # call log_datetime and returned wrapper 

"""
checking.......
Function: daily_backup
Run on: 2024-07-01 03:07:27
------------------------------
Daily backup job has finished.
"""