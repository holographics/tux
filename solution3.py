#!/usr/bin/env python
from collections import defaultdict

orders = dict(A=defaultdict(list), 
            B=defaultdict(list))


def check_count(total, days, day, count): 
    for order in days[day]:
        total = list(map(sum, zip(order, total)))

    if day == count-2:
        return total
    return check_count(total, days, day-1, count)
            

def place_order(small, medium, large, day):
    order = [small, medium, large]
    for style, days in orders.items():
        total = check_count(order, days, day, day)
        
        if all([n<=5 for n in total]):
            orders[style][day].append(order)
            return True 
    return False 


if __name__ == '__main__': 
    for day in range(1, 5):
        if place_order(small = 3, medium = 3, large = 3, day = 2):
            print ('Sufficient number is available on a day %s.' % day)
        else:
            print ('More are needed on a day %s.' % day)
