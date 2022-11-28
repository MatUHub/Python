from datetime import datetime as dt
from time import time

loge = []

def logger_calc(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        data = ''.join(data)
        file.write(f'Time: {time} Command: {data}\n')
def get_logger():
    with open('log.csv', 'r') as file:
        global loge
        for line in file:
           loge.append(line)
        
