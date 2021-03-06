#!/usr/bin/env python
from collections import defaultdict
orders = dict(A=defaultdict(list), 
            B=defaultdict(list))

def place_order(small, medium, large, day):
    for style, events in orders.items():
        total = [small, medium, large]
        for i in range(day-2, day+1):
            for event in events[i]:
                total = map(sum, zip(total, event))

        if all([n<=5 for n in total]):
            orders[style][day].append([small, medium, large])
            print 'Sufficient number of tuxedos is available on day %s' % day
            break 
    else: 
        print 'More tuxedos are needed for day %s!' % day

if __name__ == '__main__': 
    for day in range(12, 17):
        place_order(small = 0, medium = 1, large = 4, day = day)
