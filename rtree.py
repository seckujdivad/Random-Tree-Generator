class rtree:
    def __init__(self, canvas, splits=None, fruitfreq=None, species=None, x=None, y=None):
        #check data
        import tkinter
        self.canvas = canvas
        if type(self.canvas) != tkinter.Canvas:
            raise Exception('Provide a valid tkinter Canvas object')
        if splits != None:
            self.branch.splits = splits
        if fruitfreq != None:
            self.branch.fruitfreq = fruitfreq
        if species != None:
            self.species = species
        if x != None:
            self.coords.x = x
        if y != None:
            self.coords.y = y
        if self.species not in self.species_list:
            raise ValueError('Species "' + str(self.species) + '" is not in the list of species')
        if type(self.branch.splits) != int or self.branch.splits < 1: #if not an integer, the "or" statement will escape and will not perform the second piece of logic unless "splits" is an integer
            raise TypeError('splits must be an integer greater than 0')
        if self.branch.fruitfreq == True or (type(self.branch.fruitfreq) != int and type(self.branch.fruitfreq) != bool) or self.branch.fruitfreq < 1:
            raise TypeError('fruitfreq must be an integer greater than 0 or False')
        if type(self.coords.x) != int:
            raise TypeError('x must be an integer')
        if type(self.coords.y) != int:
            raise TypeError('y must be an integer')
        self._ready = True
    _ready = False #has been constructed
    class coords:
        x = 200
        y = 200
    class branch:
        splits = 2
        fruitfreq = 3
        depth = 3
        length = 30
        range = 10
        d_anglerange = 20
    class trunk:
        segments = 2
        class length:
            length = 40
            range = 10
    species = 'apple'
    species_list = ['apple']
    class fruits:
        class apple:
            colour = 'red'
            size = 15
    fruits.fruits = {'apple':fruits.apple}
    def render(self):
        import random
        if not self._ready:
            raise Exception('Need to construct module')
        def sub_iter_render(self, angle, module, random):
            angle += random.randint(0 - (module.branch.d_anglerange / 2), module.branch.d_anglerange / 2)
            length = module.branch.length + random.randint(0 - (module.brange.range / 2), module.branch.range / 2)
            for i in module.splits:
                self(self, angle, module, random)
        sub_iter_render(sub_iter_render, 0, self, random)
    def _calculate(start_x, start_y, angle, length):
        import math
        d_x = math.cos(math.radians(angle)) / length
        d_y = pow(pow(length, 2) - pow(d_x, 2), 1/2)
        return start_x + d_x, start_y + d_y
