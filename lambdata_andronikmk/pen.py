"""
Pen class
"""

class Pen():
    """ Class to determine type of pen."""
    def __init__(self, brand='uniball', color = 'Blue',
                 size='0.5', tip_style='felt'):
        self.brand = brand
        self.color = color
        self.size = size
        self.tip_style = tip_style

    def pen_type(self):
        if self.tip_style == 'felt':
            print('Gel Pen')
        else:
            print('Ink Pen')
    
