class rtree:
    def __init__(self, canvas, splits=None, fruitfreq=None, species=None, x=None, y=None):
        #check data
        import tkinter
        self.canvas = canvas
        if type(self.canvas) != tkinter.Canvas:
            raise Exception('Provide a valid tkinter Canvas object')
        if splits != None:
            self.splits = splits
        if fruitfreq != None:
            self.fruitfreq = fruitfreq
        if species != None:
            self.species = species
        if x != None:
            self.coords.x = x
        if y != None:
            self.coords.y = y
        if self.species not in self.species_list:
            raise ValueError('Species "' + str(self.species) + '" is not in the list of species')
        if type(self.splits) != int or self.splits < 1: #if not an integer, the "or" statement will escape and will not perform the second piece of logic unless "splits" is an integer
            raise TypeError('splits must be an integer greater than 0')
        if self.fruitfreq == True or (type(self.fruitfreq) != int and type(self.fruitfreq) != bool) or self.fruitfreq < 1:
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
    splits = 2
    fruitfreq = 3
    species = 'apple'
    species_list = ['apple']
    class fruits:
        class apple:
            colour = 'red'
            size = 15
    fruits.fruits = {'apple':fruits.apple}
    def render(self):
        if not self._ready:
            raise Exception('Need to construct module')
        
