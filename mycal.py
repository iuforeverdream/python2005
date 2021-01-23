#!/usr/bin/python3
from datetime import datetime
import sys

def is_leap(year):
    """判断闰年"""
    return year % 4 == 0 and year %100 !=0 or year %400 ==0


def days_of_month(year,month):
    """返回指定的年份和月份对应的天数"""
    days_list = ['', 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = days_list[month]
    return days+1 if month ==2 and is_leap(year)  else days


def main():
    if len(sys.argv) == 3:
        month, year = map(int, sys.argv[1:])
    else:
        curr_date =datetime.now()
        year, month = curr_date.year, curr_date.month
    y, m= (year -1, month +12) if month <=2 else (year, month)
    c, y =y //100, y % 100
    w = y + y // 4 + c // 4 - 2 * c + 26 * (m+1) // 10
    w %= 7
    month_names = ['','January','February','March','April','May','June',
    'July','August','September','October','November','December']
    print(f'{month_names[month]} {year}'.center(21))
    print('Su Mo Tu We Th Fr Sa')
    print(' ' * 3 * w, end ='')
    days =days_of_month(year,month)
    for day in range(1,days+1):
        print(f'{day}'.rjust(2),end=' ')
        w +=1
        if w ==7:
            w = 0
            print()
    print()
   

if __name__ == '__main__':
    main()
