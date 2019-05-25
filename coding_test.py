SIZES = ['small', 'medium', 'large']
STYLES = ['A', 'B']

class Tuxedo(object):
    def __init__(self, style, size):
        self.style = style
        self.size = size
        self.day = int() 
    
    def __str__(self):
        return '%s %s' % (self.size, self.style)

    def set_day(self, day):
        self.day = day 

    def is_available(self, day):
        return any([not self.day, self.day + 3 < day]) 

class Inventory(object):
    def __init__(self):
        self.tuxedos = [Tuxedo(style, size) for size in SIZES for m in range(5) for style in STYLES]

    def get_tuxs(self, style, size, day):
        return [tux for tux in self.tuxedos if tux.style == style and tux.size == size and tux.is_available(day)]

    def place_order(self, small, medium, large, day):
        for style in STYLES:
            stock = dict()
            for size in SIZES:
                stock[size] = self.get_tuxs(style, size, day)

            if len(stock['small']) >= small and len(stock['medium']) >= medium and len(stock['large']) >= large:
                [tux.set_day(day) for size, tuxs in stock.items() for tux in tuxs]
                print 'Tuxedos style %s are available for day %s' % (style, day)
                break
        else:
            print 'We need more tuxedos!'

if __name__ == '__main__': 
    inv = Inventory()
    for i in range(1, 9):
        inv.place_order(small = 4, medium = 0, large = 3, day = i)
